# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

def kmp_search(text, pattern):
  def build_partial_match_table(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0:
          length = lps[length - 1]
        else:
          lps[i] = 0
          i += 1

    return lps

  n = len(text)
  m = len(pattern)
  lps = build_partial_match_table(pattern)

  i, j = 0, 0

  while i < n:
    if pattern[j] == text[i]:
      i += 1
      j += 1
    
    if j == m:
      print(f"Pattern found at index {i - j}")
      j = lps[j - 1]
    
    elif i < n and pattern[j] != text[i]:
      if j != 0:
        j = lps[j - 1]
      else:
        i += 1