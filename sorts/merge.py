# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/

def merge(arr, low, high):
  tmp = []
  mid = (low + high) // 2
  i, j = low, mid + 1

  while i <= mid and j <= high:
    if arr[i] <= arr[j]:
      tmp.append(arr[i])
      i += 1
    else:
      tmp.append(arr[j])
      j += 1
    
  while i <= mid:
    tmp.append(arr[i])
    i += 1
  
  while j <= high:
    tmp.append(arr[j])
    j += 1
  
  for k in range(low, high + 1):
    arr[k] = tmp[k - low]
  
  return arr

def merge_sort(arr, low, high):
  if (low >= high): return

  mid = (low + high) // 2

  merge_sort(arr, low, high)
  merge_sort(arr, mid + 1, high)

  sorted_array = merge(arr, low, high)

  return sorted_array
