# fundamentals

# JS Data Types: Numbers, Strings, Booleans, Null, NaN, Undefined
# Python Data Types: (int) whole, (float) decimal, String, Boolean, None


first_name = "Matilda"
age = 12
psychic_powers = True
final_grade = 3.2

# 'age' + 2 (age2)
print("Hello my name is " + first_name + str(age))
print(f"Hello my name is {first_name}")

# conditionals

if age > 20:
    print("Is True!")
elif age < 20:
    print("Is False!")


# lists
vacation_destinations = ["To Bed", "Germany", "Israel", "Spain", "Greece"]

print(vacation_destinations[0])

vacation_destinations.append("Japan")
print(vacation_destinations)


# dictionaries

sampleDict = {"first_name": "Matilda", "age": 12}

print(sampleDict["age"])

# Loops

for destination in vacation_destinations:
    print(destination)
    for l in destination:
        print(l)
