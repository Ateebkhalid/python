print("Welcome to my calculator")
num1=int(input("Enter the first number ="))
num2=int(input("Enter the second number="))
print("Please select an operator")
print("For Addition please press 1")
print("For subtraction please press 2")
print("For multiplication please press 3")
print("For division please press 4")
choice =input("Select number 1/2/3/4=")
if choice == '1':
    print(num1,'+',num2, '=', (num1+num2))
 elif choice =="2"
        print(num1, '-', num2, '=',(num1-num2))
