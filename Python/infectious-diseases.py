import virus

population = 10000
infected = 1
can_catch_virus = population - infected
contacts_per_day = 10

for day in range(90):
    # Infected chickens spread the virus to those who haven't already had it.
    newly_infected = virus.spread(
        infected, can_catch_virus, population, contacts_per_day
    )
    infected = infected + newly_infected
    can_catch_virus = can_catch_virus - newly_infected

    newly_recovered = virus.recover(infected)
    infected -= newly_recovered

    if day == 13:
        contacts_per_day = 3
    
    print(str(infected) + " chickens infected.")

    if infected == 0:
        break

print("----------")
print(str(population - can_catch_virus) + " chickens caught the virus.")

