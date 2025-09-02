def numbers(a: int):
  Series = []
  for i in range(a):
    Series.append(2*i+1)
  return Series
a = int(input("enter a number(greater than 0):"))
result = numbers(a)
print("Output:",",".join(map(str, result)))
