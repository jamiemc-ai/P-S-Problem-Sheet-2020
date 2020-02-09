# This program calculate BMI

Weight = float(input("enter your weight in KG;"))
Height = float(input("enter height in cm;"))

Heightsquared = (Height*Height)
BMI= Weight / Heightsquared
print("Your BMI is",BMI,"based on the figures you have been provided")
