#variable declaration
a = input ("Enter first number: ")
b = input ("Enter second number: ")
#perform a mathematical opertaion
operaton = input ( "Enter operation (+, -, *, /): ")
if operaton == "+":
    result = float(a) + float(b)
    print("The sum of", a, "and", b, "is", result)
elif operaton == "-":
    result = float(a) - float(b)
    print("The difference between", a, "and", b, "is", result)                  
elif operaton == "*":
    result = float(a) * float(b)
    print("The product of", a, "and", b, "is", result)     
elif operaton == "/":
    if float(b) != 0:
        result = float(a) / float(b)
        print("The division of", a, "by", b, "is", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")