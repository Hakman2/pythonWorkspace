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
number = [1, 3, 7, 2, 4, 90, 87, 6, 54, 22, 23, 24, 25]

for num in range(len(number)):
    if number[num] % 2 == 0:
        time.sleep(0.5)
        print("even -->", num, number[num])

for num in range(len(number)):
    if number[num] % 2 != 0:
        time.sleep(0.5)
        print("odd -->", num, number[num])
