# hello_world.py
# A simple Hello World script for Python coding studies

# name = "Hak"
# age = 25
# print("Hello, World!" +" "+"My name is" +" "+ name +". "+" I am "+  str(age) + "years old")

# day = int(input("Enter your number: "))

# if day == 1:
#     print("Monday")

# elif day == 2:
#     print("Tuesday")

# elif day == 3:
#     print("Wednesday")

# elif day == 4:
#     print("Thursday")

# elif day == 5:
#     print("Friday")
    
# else: 
#     print("Enter number from 1 to 5.")

# # Or

# days = {1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday"}

# # day = int(input("Enter your number(1-5): "))
# # print(days.get(day,"Enter number from 1 to 5."))

import time
# number = [1, 3, 7, 2, 4, 90, 87, 6, 54, 22, 23, 24, 25]

# for num in range(len(number)):
#     if number[num] % 2 == 0:
#         time.sleep(0.5)
#         print("even -->", num, number[num])

# for num in range(len(number)):
#     if number[num] % 2 != 0:
#         time.sleep(0.5)
#         print("odd -->", num, number[num])

# while True:
#     command = input("enter a command: ")
#     if command == "e":
#         break
# c = 0
# while c != 100:
#     c += 1
#     print(c)
#     if c == 100:
#         break

# even = 0

# while even != 1000:
#         even += 1
#         if even % 2 == 0:
#             print("Even -->", even)
#         pass

# number = [1,56,234,87,4,76,24,69,90,135]
# def is_even(num):
#     for num in range(len(number)):
#         if number[num] % 2 == 0:
#             print("even --> ", number[num])
# is_even(5)


try:
    takenum = int(input("Enter a number from 1-100000: "))

    def is_even(takenum):
        if takenum % 2 == 0:
            print("even")
        elif takenum % 2 != 0:
            print("Old")
    is_even(takenum)
except ValueError:
    print("try again!!!")

    

    
