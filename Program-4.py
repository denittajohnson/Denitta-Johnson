def multiples(numbers):
    result = {}
    for i in range(1, 10): 
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

numbers = list(map(int, input("enter numbers(separated by space): ").split()))

output = multiples(numbers)
print(output)