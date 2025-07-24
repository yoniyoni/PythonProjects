number1=input("Enter first number: ")
number2=input("Enter second number: ")  
operation=input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = float(number1) + float(number2)    
elif operation == '-':
    result = float(number1) - float(number2)        
elif operation == '*':
    result = float(number1) * float(number2)    
elif operation == '/':
    if float(number2) != 0:
        result = float(number1) / float(number2)
    else:
        result = "Error: Division by zero"  
else:
    result = "Error: Invalid operation" 

print(f"Result of {number1} {operation}{number2} is :", result)