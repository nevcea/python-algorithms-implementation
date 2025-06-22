# https://velog.io/@rhfo0509/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A0%95%EB%A0%AC-%EB%B8%8C%EB%A3%A8%ED%8A%B8-%ED%8F%AC%EC%8A%A4%EB%B2%95%EB%B3%B4%EC%9D%B4%EC%96%B4%EB%AC%B4%EC%96%B4%EB%B2%95

def preprocess_bad_char(pattern):
  bad_char = {}
  m = len(pattern)

  for i in range(m):
    bad_char[pattern[i]] = i

  return bad_char

def match(text, pattern):
  bad_char = preprocess_bad_char(pattern)
  n, m = len(text), len(pattern)
  s =  0
  
  while s <= n - m:
    j = m - 1
    
    while j >= 0 and text[s + j] == pattern[j]:
      j -= 1
    
    if j < 0:
      return s

    shift = max(1, j - bad_char.get(text[s + j], -1))
    s += shift
  
  return -1