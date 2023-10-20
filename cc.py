num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division")
op = int(input("Enter number for the operator"))
if op==1:
    print("Addition")
    value = num1+num2
    print(value)
elif op==2:
    print("Subtraction")
    value = num1-num2
    print(value)
elif op==3:
    print("Multiplication")
    value = num1*num2
    print(value)
elif op==4:
    print("Division")
    value = num1/num2
    print(value)
else:
    print("Invalid Operator")