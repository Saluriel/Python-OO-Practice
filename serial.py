"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initialize the start variable and the variable used to increment"""
        self.start = start
        self.increment = start
        
    def __repr__(self):
        """Returns the start input"""
        return f"<SerialGenerator start = {self.start}, next = {self.increment+1}>"

    def generate(self):
        """Increments the starting number by 1"""
        print(self.increment)
        self.increment += 1
    
    def reset(self):
        """Resets the number back to the starting input number"""
        self.increment = self.start