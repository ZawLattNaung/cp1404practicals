import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()  # Sort guitars by year using __lt__ method
    display_guitars(guitars)

    # Add new guitars from user input
    print("\nAdd a new guitar (leave name empty to finish):")
    new_guitar = add_guitar()
    while new_guitar is not None:
        guitars.append(new_guitar)
        new_guitar = add_guitar()

    # Save all guitars back to file
    save_guitars(FILENAME, guitars)
    print("\nGuitars have been saved to", FILENAME)

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    pass

def add_guitar():
    pass

def save_guitars(filename, guitars):
    pass


if __name__ == "__main__":
    main()