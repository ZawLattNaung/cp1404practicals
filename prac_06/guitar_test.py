from guitar import Guitar
#using get age method to test
guitar1 = Guitar("Gibson L-5 CES", 1922, 500)
guitar2 = Guitar("Another Guitar", 2013, 1000)
expected_age_gibson = 103
actual_age_gibson = guitar1.get_age()
print(f"{guitar1.name} get_age() - Expected {expected_age_gibson}. Got {guitar1.get_age()}")

expected_age_another = 12
actual_age_another = guitar2.get_age()
print(f"{guitar2.name} get_age() - Expected {expected_age_another}. Got {guitar2.get_age()}")

