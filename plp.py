#creating a basic calculator program with pyhton

#user input 
num1= float(input("enter a number: "))
num2= float(input("enter another number: "))
operator=input("enter the operator(+, -, *, /): ")

#perform the operation and display the result 
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"{num1} + {num2} = {result}")

elif operator == '*': 
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


elif operator == '/':   
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} + {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")