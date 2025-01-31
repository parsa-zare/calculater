import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Negative root"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error: Negative factorial"
    return math.factorial(x)

def log(x, base=10):
    if x <= 0:
        return "Error: Log of non-positive number"
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def calculator():
    print("Advanced Python Calculator")
    print("Operations: +, -, *, /, ^, sqrt, fact, log, sin, cos, tan")
    
    while True:
        operation = input("Enter operation (or 'exit' to quit): ")
        
        if operation == "exit":
            break
        
        if operation in ['+', '-', '*', '/', '^']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            elif operation == '^':
                print("Result:", power(num1, num2))
        
        elif operation in ['sqrt', 'fact', 'log', 'sin', 'cos', 'tan']:
            num = float(input("Enter number: "))
            if operation == 'sqrt':
                print("Result:", sqrt(num))
            elif operation == 'fact':
                print("Result:", factorial(int(num)))
            elif operation == 'log':
                base = float(input("Enter base (default 10): ") or 10)
                print("Result:", log(num, base))
            elif operation == 'sin':
                print("Result:", sin(num))
            elif operation == 'cos':
                print("Result:", cos(num))
            elif operation == 'tan':
                print("Result:", tan(num))
        else:
            print("Invalid operation!")

if __name__ == "__main__":
    calculator()
