# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def percentage(x, y):
    return (x * y) / 100




from calculator import add, subtract, multiply, divide, percentage

# Example usage
result_add = add(5, 3)
result_subtract = subtract(10, 4)
result_multiply = multiply(2, 6)
result_divide = divide(8, 2)
result_percentage = percentage(50, 20)

print(result_add, result_subtract, result_multiply, result_divide, result_percentage)

output:-
![WhatsApp Image 2024-07-21 at 23 02 57_96c3b654](https://github.com/user-attachments/assets/ad544e79-b564-435b-ba64-a6624bf8688a)
