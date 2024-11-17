for number in range(100, 0, -1):  
    if number > 0:
        print(f"{number} is positive", end=", ")
        if number % 2 == 0:
            print("and even.")
        else:
            print("and odd.")
