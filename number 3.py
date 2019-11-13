x = float(input("перша цифра: "))
y = float(input("друга цифра: "))
operation = input("Operation: ")

result = None

if operation == "+":
    result = x + y
if operation == "-":
        result = x - y
if operation == "*":
            result = x * y
if operation == "/":
                result = x / y
else:
                print("unsupported operation")
if result is not None:
                    print("Result: ", result)