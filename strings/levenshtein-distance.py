def levenshtein_distance(t1, t2):
  r, c = len(t1) + 1, len(t2) + 1
  arr = [
    list(range(c)) if not i else [i] + [0] * (c - 1)
    for i in range(r)
  ]

  for i in range(1, r):
    for j in range(1, c):
      if t1[i - 1] == t2[j - 1]:
        arr[i][j] = arr[i-1][j-1]
      else:
        arr[i][j] = min(
          arr[i-1][j],
          arr[i][j-1],
          arr[i-1][j-1],
        ) + 1
  
  for r in arr:
    print(r)

  return arr[r - 1][c - 1]