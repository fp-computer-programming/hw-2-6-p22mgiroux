# Author: MOG 9/21/21

f_temp = input("What is the temperature in fahrenheit? ")

c_temp = (int(f_temp) - 32) * (5 / 9)

fs = "s"
if(f_temp == "1"): fs = ""
cs = "s"
if(c_temp == 1): fs = ""

print("{} degree{} fahrenheit is equal to {} degree{} celcius.".format(f_temp, fs, c_temp, cs))