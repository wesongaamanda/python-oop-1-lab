class Coffee:
    """Represents a coffee with a size and price."""

    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        
        self.size = size
       
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """Prints a tip message and increases the price by 1."""
        print("This coffee is great, here's a tip!")
        self.price += 1