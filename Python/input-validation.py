thirty_one = [1, 2, 3, 5, 7, 8, 10, 12]

day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month > 12 or month < 1:
    print("Error. Month must be between 1 and 12.")

if month not in thirty_one and day > 30:
    print("Error. Day must be within the month.")

birth_year = int(input("Enter a birth year: "))
birth_year_length = len(str(abs(birth_year)))
if birth_year_length != 4:
    print("Error. Year must have four digits.")

