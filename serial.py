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

    """create counter with start number"""
    def __init__(self,start):
        self.start = start
        self.next =  start

    """creates future value and returns current"""
    def generate(self):
        self.next = self.next + 1
        current = self.next - 1
        return current

    """returns starting number"""
    def reset(self):
        self.next = self.start
