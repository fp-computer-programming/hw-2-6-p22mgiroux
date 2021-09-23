# Author: MOG 9/23/21

pi = 3.14159

rad = input("What is the radius of your cylinder? ")
height = input("What is the height of your cylinder? ")

volume = pi * int(rad) ** 2 * int(height)
surf_area = 2 * pi * int(rad) * (int(height) + int(rad))

print("Volume: " + str(volume))
print("Surface Area: " + str(surf_area))