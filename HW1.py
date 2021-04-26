# Takes a year as an input from the user

# Handles non-integer values
i = 0
while i == 0:
    try:
        year = int(input("Give me a year. (Input an integer): "))
        i = 1
    except:
        print("Sorry, that isn't a valid year")

# calculates whether that year is a leap year and outputs it
if (year % 400) == 0:
    print(year, "is a leap year")
elif (year % 4) == 0:
    if (year % 100) == 0:
        print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
     print(year, "is not a leap year")
