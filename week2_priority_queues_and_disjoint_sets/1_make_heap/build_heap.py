# python3


class MinHeap:
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    
    def shift_down(self, index, return_swaps=False):
        swaps = []
        max_index = index
        while True:
            left_index = 2*index + 1
            right_index = 2*index + 2
            if left_index < self.size and self.data[left_index] < self.data[max_index]:
                max_index = left_index
            
            if right_index < self.size and self.data[right_index] < self.data[max_index]:
                max_index = right_index
            
            if index != max_index:
                swaps.append((index, max_index))
                self.data[index], self.data[max_index] = self.data[max_index], self.data[index]
                index = max_index
            else:
                break
        
        if return_swaps:
            return swaps

    
    def build_heap(self):
        swaps = []
        for index in range((self.size-1) // 2, -1, -1):
            swaps.extend(self.shift_down(index, return_swaps=True))
        return swaps
        

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    min_heap = MinHeap(data)
    return min_heap.build_heap()


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
