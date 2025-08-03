from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi with fanciness and flagfall added."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
