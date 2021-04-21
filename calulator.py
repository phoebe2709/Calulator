def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
    
value1 = int(input("Enter 1st number: "))
value2 = int(input("Enter 2nd number: "))

print("Select 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division")
select = int(input("Choose operation 1/2/3/4: "))

if select == 1:
    print(value1, "+", value2, "=", addition(value1, value2))
    
elif select == 2:
   print(value1, "-", value2, "=", subtraction(value1, value2))
   
elif select == 3:
   print(value1, "*", value2, "=", multiplication(value1, value2))
elif select == 4:
   print(value1, "/", value2, "=", divide(value1, value2))
   
else:
   print("Enter correct operation")