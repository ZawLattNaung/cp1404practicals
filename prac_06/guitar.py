"""
estimated time=15mins
actual time=
"""


"""
creating class for guitar
"""
class Guitar:
    def __init__(self,name="",year=0,cost=0):
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self): #adding __str__
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):#adding get_age to calculate guitar age
        current_year = 2025  # use datetime to get the current year
        return current_year - self.year