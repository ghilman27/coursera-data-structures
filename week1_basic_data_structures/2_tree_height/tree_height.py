# python3

import sys
import threading
from collections import deque


class Node:
    def __init__(self, parent=None, children=None):
        self.parent = parent
        self.children = []
        if children:
            self.children.extend(children)
    
    def add_child(self, child):
        self.children.append(child)
    
    def set_parent(self, parent):
        self.parent = parent


class Tree:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = []
        if nodes:
            self.nodes.extend(nodes)

    def set_root(self, root):
        self.root = root
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def compute_height(self):
        if len(self.nodes) == 0:
            return 0
        
        queue = deque()
        queue.append(self.root)
        height = 0
        level_nodes = 1
        while len(queue) > 0:
            node = queue.popleft()
            level_nodes -= 1
            for child in node.children:
                queue.append(child)
            if level_nodes == 0:
                height += 1
                level_nodes = len(queue)
        
        return height


def allocate_nodes(parents):
    nodes = []
    for parent in parents:
        nodes.append(Node())
    return nodes


def link_nodes(n, nodes, parents):
    root_node_idx = -1
    if n != len(nodes) or n != len(parents):
        raise Exception('Please input the same number of nodes and parents')

    for child_idx, parent_idx in enumerate(parents):
        if parent_idx == -1:
            root_node_idx = nodes[child_idx]
        else:
            child_node = nodes[child_idx]
            parent_node = nodes[parent_idx]
            child_node.set_parent(parent_node)
            parent_node.add_child(child_node)
    
    return root_node_idx, nodes


def compute_height(n, parents):
    nodes = allocate_nodes(parents)
    root_node, nodes = link_nodes(n, nodes, parents)
    tree = Tree(root=root_node, nodes=nodes)
    return tree.compute_height()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == '__main__':
    main()

