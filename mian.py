

# age = int(input("Enter your age: "))


# if age >= 18:
#     print("you are now signed up")
# elif age == 0:
#     print("you haven't be born yet")
# else:
#     print("you must be 18+ to sign up")


# response = input("would you like some food?: ").lower()

# if response == "yes":
#     order = input("what would you like to eat?: ")
#     print(f"you order {order}")
# else response == "no":
#     print("okkkeyyyyyy ")


# weight conversion

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or pounds? (K or L)").lower()

# if unit == "k":
#     weight = weight * 2.205
#     unit = " Lbs"
#     print(f"your weight is {round(weight, 0)} {unit}")
# elif unit == "l":
#     weight = weight / 2.205
#     unit = " Kg"
#     print(f"your weight is {round(weight, 0)} {unit}")
# else:
#     print(f"{unit} was not valid unit")


# temperature conversion


unit = input("Celsius or Fahrenheit? (C or F)").lower()

temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = (temp * 9/5) + 32
    unit = " Fahrenheit"
    print(f"the temperature is {round(temp, 2)} {unit}")
elif unit == "f":
    temp = (temp - 32) * 5/9
    unit = " Fahrenheit"
    print(f"the temperature is {round(temp, 2)} {unit}")
else:
    print(f"Enter a valid {unit}")
