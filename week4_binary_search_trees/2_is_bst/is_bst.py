#!/usr/bin/python3

import sys, threading
from collections import namedtuple

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
Node = namedtuple('Node', 'key left right')

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
    return True
  
  crnt_node = tree[0]
  prev_val = -sys.maxsize
  stack = []

  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      if crnt_node.left != -1:
        crnt_node = tree[crnt_node.left]
      else:
        crnt_node = None
    
    elif stack:
      crnt_node = stack.pop()
      if prev_val > crnt_node.key:
        return False
      prev_val = crnt_node.key
      if crnt_node.right != -1:
        crnt_node = tree[crnt_node.right]
      else:
        crnt_node = None
    
    else:
      break
  
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for _ in range(nodes):
    [a, b, c] = map(int, sys.stdin.readline().strip().split())
    tree.append(Node(a, b, c))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
