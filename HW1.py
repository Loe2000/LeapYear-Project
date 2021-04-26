# Takes a year as an input from the user
year = int(input("Give me a year: "))

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
