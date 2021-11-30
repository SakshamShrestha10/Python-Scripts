while(True):
    num1 = float(input("Enter first number: "))
    if num1 == 'quit':
        exit()
    operator = input("Enter opeartor: ")
    num2 = float(input("Enter second number: "))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Error")

#while(True):
 #   num1 = float(input("Enter first number:"))
  #  operator = input("Enter operator :")
   # num2 = float(input("Enter second number: "))
    #if num2 == 'quit':
     #   exit()
    #if operator == "+":
     #   print(num1 + num2)
    #elif operator == "-":
     #   print(num1 - num2)
    #elif operator == "*":
     #   print(num1 * num2)
    #elif operator == "/":
     #   print(num1 / num2)
    #else:
      #  print("Error")


