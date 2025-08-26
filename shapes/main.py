from circle import is_area, is_circumference
from rectangle import is_areaOfrec, is_pariOfrec

# Circle
result_circle_area = is_area(4)
result_circle_circumference = is_circumference(7)

# Rectangle
result_rec_area = is_areaOfrec(8, 5)
result_rec_parimeter = is_pariOfrec(8, 5)

# Printing
print(result_circle_area,"cm")
print(result_circle_circumference, "cm")
print(result_rec_area, "cm^2" )
print(result_rec_parimeter, "cm")


# Examples
print(is_palindrome("madam"))       # True
print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("Nurses run"))  # True


