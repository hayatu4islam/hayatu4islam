# This function returns the highest of three numbers
def highestNumber(a, b, c):
  result = a
  if a < b:
    result = b
  if result < c:
    result = c
  return result
print(highestNumber(3, 7, 5))