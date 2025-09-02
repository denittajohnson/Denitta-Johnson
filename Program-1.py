class Calculator:
  def __init__(self, a: float, b: float, operation: str):
    self.a = a
    self.b = b
    self.operation = operation
  def calculate(self):
    if self.operation == '+':
      return self.a + self.b
    elif self.operation == '-':
      return self.a - self.b
    elif self.operation == '*':
      return self.a * self.b
    elif self.operation == '/':
      if self.a != 0 or self.b != 0:
        return self.a / self.b
      else:
        return "Error"
    elif self.operation == '^':
      return self.a ** self.b
    else:
      return "Invalid Operation"

a = float(input("enter first number:"))
b = float(input("enter second number:"))
op = input("enter operation(+,-,*,/,^):")
calc = Calculator(a, b, op)
result = calc.calculate()
print(result)