"""
CP1404/CP5632 - Practical
Broken program to determine score status




score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""
score = float(input("Enter score: "))
while score<0 or score>100:
    print("Enter a valid score :)")
    score = float(input("Enter score: "))
if score>90:
    print("Excellent!")
elif score>=50:
    print("Passed!")
else:
    print("Bad")




