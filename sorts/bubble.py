# https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/

def bubble_sort(arr):
  for i in range(len(arr) - 1, 0, -1):
    swapped = False

    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True

    if not swapped:
      break