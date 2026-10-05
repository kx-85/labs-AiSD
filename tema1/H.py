class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sq(self):
        return self.x ** 2 + self.y ** 2

    def __str__(self):
        return f"{self.x} {self.y}"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].sq() <= right[j].sq():
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr


n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))
sorted_points = merge_sort(points)
for p in sorted_points:
    print(p)
