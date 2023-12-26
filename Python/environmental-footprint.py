footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    footprint = footprint + 5
    eats_meat = input("Does your pet's food contain meat (yes/no)? ")
    if eats_meat == "yes":
        footprint = footprint + 10

days = int(input("How many days a week do you commute to school or work? "))
if days > 0:
    transportation = input("Do you commute by foot, bike, bus, train, or car? ")

    # Different methods of transportation have different environmental impacts.
    if transportation == "car":
        footprint = footprint + (8 * days)
    elif transportation == "bus" or transportation == "train":
        footprint = footprint + (4 * days)
    elif transportation == "bike" or transportation == "foot":
        footprint = footprint + days

print("Your environmental footprint score is " + str(footprint) + ".")

