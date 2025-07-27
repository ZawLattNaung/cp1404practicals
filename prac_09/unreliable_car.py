import random
from prac_09.car import Car

class UnreliableCar(Car):
    """An Unreliable Car that may not drive every time."""

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel=fuel, name=name)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car, depending on reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0  # Car failed to drive
