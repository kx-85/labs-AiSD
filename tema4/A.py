import sys

class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._sift_up(self.size)

    def _sift_up(self, i):
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def extract(self):
        if self.size == 0:
            return None
        max_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._sift_down(1)
        return max_val

    def _sift_down(self, i):
        while 2 * i <= self.size:
            left = 2 * i
            right = 2 * i + 1
            largest = left
            if right <= self.size and self.heap[right] > self.heap[left]:
                largest = right
            if self.heap[i] < self.heap[largest]:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

  
  input_data = sys.stdin.read().split()
  if not input_data:
      return
  n = int(input_data[0])
  heap = MaxHeap()
  idx = 1
  output = []
  for _ in range(n):
      command = input_data[idx]
      idx += 1
      if command == '0':
          val = int(input_data[idx])
          idx += 1
          heap.insert(val)
      elif command == '1':
          output.append(str(heap.extract()))
  print('\n'.join(output))
