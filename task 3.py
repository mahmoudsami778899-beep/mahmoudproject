
def is_prime(n):
    if n <= 1:
        return False  
    return True




# calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    else:
        return "Invalid operation!"




number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")







a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculator(a, b, operation)
print("Result:", result)
