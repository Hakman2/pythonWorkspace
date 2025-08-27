try:
    colorNumber1 = int(input("Enter First number(1 to 4): "))
    colorNumber2 = int(input("Enter Second number(1 to 4): "))
    print(f"Your selected numbers are {colorNumber1} and {colorNumber2}")
       
    if (colorNumber1 == 1 and colorNumber2 == 1 or  colorNumber1 == 1 and colorNumber2 == 3 or colorNumber1 == 2 and colorNumber2 == 3 or  colorNumber1 == 3 and colorNumber2 == 2):
        print("Red")
    elif(colorNumber1 == 1 and colorNumber2 == 2 or  colorNumber1 == 3 and colorNumber2 == 1 or colorNumber1 ==3 and colorNumber2 == 4) :
        print("Green")
    elif(colorNumber1 == 2 and colorNumber2 == 1  or  colorNumber1 == 2 and colorNumber2 == 4 or colorNumber1 == 3 and colorNumber2 == 3 or colorNumber1 == 4 and colorNumber2 == 2):
        print("Yellow")
    elif(colorNumber1 == 1 and colorNumber2 == 4  or  colorNumber1 == 2 and colorNumber2 == 2 or colorNumber1 == 4 and colorNumber2 == 1 or colorNumber1 == 4 and colorNumber2 == 3):
        print("Blue")
    else:
        print("Enter number from 1 to 4")
    
except ValueError:
    print("Invalid Entery: Enter required numbers")
