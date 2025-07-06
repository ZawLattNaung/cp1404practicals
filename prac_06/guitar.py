"""
estimated time=15mins
actual time=
"""


"""
creating class for guitar
"""
class Guitar:
    def __init__(self,name="",year="",cost=0.0):
        self.name=name
        self.year=year
        self.cost=cost
    def __str__(self): #adding __str__
        return f"{self.name} ({self.year}) : ${self.cost}"