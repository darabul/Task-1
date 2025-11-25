a = float(input("Первое число: "))
b = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+": print(a + b)
elif operation == "-": print(a - b)
elif operation == "*": print(a * b)
elif operation == "/": print(a / b if b != 0 else "Ошибка!")
else: print("Неизвестная операция")# could you calculate this
new-edit-calculator.py
