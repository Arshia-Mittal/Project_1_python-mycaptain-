# Area of circle (task 1)

import math
r = float(input("Enter radius of circle: "))
area = r* r* math.pi
print("Area of the circle is ",area) 


# Take input of filename and print its extension as output (task 2)

filename = input("Input the filename: ")
f_extns = filename.split(".")
print("The extention of the file is : " + repr(f_extns[-1]))
