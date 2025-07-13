"""
estimated time=15mins
actual time=20mins
"""


"""
creating class for guitar
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50
class Guitar:
    def __init__(self,name="",year=0,cost=0):
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self): #adding __str__
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):#adding get_age to calculate guitar age
          # use datetime to get the current year
        return CURRENT_YEAR - self.year

    def is_vintage(self):#determine vintage
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year