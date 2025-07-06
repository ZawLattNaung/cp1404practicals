from guitar import Guitar

print("My guitars!")
guitars = []

# get name
name = input("Name: ")

# Only enter loop if name is not empty
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")

    # Ask again at the end of the loop
    name = input("Name: ")


