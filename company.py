from load_files import update_data
from data_point import Data_Point
import csv
class Company:
    """
    Represents a Company
    """
    def __init__(self, id: str):
        """
        Initialize a new company
        """
        self.id = id
        self.storage = []


        try:
            self.populate_storage()
        except:
            update_data(id)
            self.populate_storage()
    def populate_storage(self):
        """
        Fills up self.storage with data points
        """
        path = 'company_library/' + self.id + '.csv'
        with open(path,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                temp_volume = line[5]
                temp_price = line[4]
                temp_date = line[0]
                new_point = Data_Point(temp_date, temp_price, temp_volume)
                self.storage.append(new_point)
        self.storage.pop(0)



if __name__ == "__main__":
    for i in IBM.storage:
        print(i)