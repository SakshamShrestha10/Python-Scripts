while(True):
    name = input("Enter your name: ")
    if name == 'quit':
        exit()
    Your_Score = float(input("Enter your score: "))

    if Your_Score >= 75 and Your_Score <= 100:
        print("Congratulations! You have passed with distinction")

    elif Your_Score >= 65 and Your_Score <= 74:
        print("Congratulations! You have passed with first division")

    elif Your_Score >= 55 and Your_Score <= 64:
        print("Congratulations! You have passed with second division")

    elif Your_Score >= 40 and Your_Score <= 54:
        print("Congratulations! You have passed with third division")
    
    else:
        print("Sorry! You have failed")
