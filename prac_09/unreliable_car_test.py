from unreliable_car import UnreliableCar

def test_unreliable_car():
    car = UnreliableCar("Test", 100, 50)

    total_driven = 0
    attempts = 100
    for _ in range(attempts):
        total_driven += car.drive(1)

    print(f"Tried to drive {attempts} times. Actually drove: {total_driven} km.")

test_unreliable_car()
