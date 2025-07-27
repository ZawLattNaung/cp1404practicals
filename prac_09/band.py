"""Band class for CP1404 - demonstrating association (Band has Musicians)."""


class Band:
    """Band class represents a group of musicians."""

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the band and its members."""
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def add(self, musician):
        """
        Add a musician to the band.
        """
        self.members.append(musician)

    def play(self):
        """
        Return a string showing each band member playing their instrument.
        """
        return "\n".join(member.play() for member in self.members)