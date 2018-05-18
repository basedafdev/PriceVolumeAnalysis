class data_point:
    """
    Represent a data point
    """
    def __init__(self, date, volume, price):
        """
        Initialize a new data_point
        """
        self.date = date
        self.volume = volume
        self.price = price
