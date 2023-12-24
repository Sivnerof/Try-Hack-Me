material = input("What material is it? ")
length = float(input("What is its length in cm? "))

waste_type = "recycling" if material == "plastic" and length >= 7.5 else "trash"

print("Please deposit your item in the " + waste_type + " bin.")

