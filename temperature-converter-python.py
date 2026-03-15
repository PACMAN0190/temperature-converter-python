unit = input("is this temperature celsius or fahrenheit (c/f): ")
temp = float(input("enter the temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"the temperature in Fahrenheit is: {temp}F")

elif  unit == "f":
    temp = round((9 / temp) * 5 - 32, 1)
    print(f"the temperature in celsius is : {temp}c")

else :
    print(f"{unit}is not a valid unit")
