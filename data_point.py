class Data_Point:
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
    def __str__(self):
        """
        Return a string representation of a point
        :return:
        """
        return "data: " + str(self.date) + " || volume: " + str(self.volume) + " || price: " + str(self.price)
if __name__ == "__main__":
    x = Data_Point(2,3,4)
    print(x)