# python3
import sys
from collections import deque

class QueueWithMax():
    def __init__(self):
        self.__queue = deque()
        self.max = deque([])
    
    def __len__(self):
        return(len(self.__queue))

    # O(n) [WORST]
    def enqueue(self, a):
        self.__queue.append(a)
        if len(self.max) == 0:
            self.max.append(a)
        else:
            while len(self.max) > 0 and self.max[-1] < a:
                self.max.pop()
            self.max.append(a)
    
    # O(1)
    def dequeue(self):
        assert(len(self.__queue))
        popped_value = self.__queue.popleft()
        if popped_value == self.max[0]:
            self.max.popleft()

    # O(1)
    def max(self):
        assert(len(self.__queue))
        return self.max[0]


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window(sequence, m):
    queue = QueueWithMax()
    result = []

    # O(n + n/m*m) --> O(n)
    for value in sequence:
        if len(queue) < m:
            queue.enqueue(value)
        if len(queue) == m:
            result.append(queue.max())
            queue.dequeue()
    return result


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

