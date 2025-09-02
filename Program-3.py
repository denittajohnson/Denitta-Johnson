def numbers(a: int):

  if a % 2 != 0:
    num = a
  else:
    num = a-1

  Series = []
  for i in range(num):
    Series.append(2*i+1)
  return Series
a = int(input("enter a number(greater than 0):"))
result = numbers(a)
print("Output:",",".join(map(str, result)))