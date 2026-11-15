class HeapSorter:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def _sift_down(self, start, end):
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap = root

            if self.arr[swap] < self.arr[child]:
                swap = child

            if child + 1 <= end and self.arr[swap] < self.arr[child + 1]:
                swap = child + 1

            if swap == root:
                return
            else:
                self.arr[root], self.arr[swap] = self.arr[swap], self.arr[root]
                root = swap

    def sort(self):
        for start in range((self.n - 2) // 2, -1, -1):
            self._sift_down(start, self.n - 1)

        for end in range(self.n - 1, 0, -1):
            self.arr[0], self.arr[end] = self.arr[end], self.arr[0]
            self._sift_down(0, end - 1)

        return self.arr


n = int(input())
arr = list(map(int, input().split()))
sorter = HeapSorter(arr)
sorted_arr = sorter.sort()
print(' '.join(map(str, sorted_arr)))
