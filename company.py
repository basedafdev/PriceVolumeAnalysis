from load_files import update_data
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
        self.dates = []
        self.volumes = []
        self.close_prices = []
        self.open_prices = []
        self.market_cap  = 0
        self.get_market_cap()
        self.populate_storage()
    def populate_storage(self):
        """
        Fills up self.dates,volumes,and prices with info
        """
        path = 'company_library/' + self.id + '.csv'
        try:
            with open(path,'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    temp_volume = line[8]
                    temp_close_price = line[2]
                    temp_open_price = line[6]
                    temp_date = line[1]
                    try:
                        temp_dates = temp_date.split("-")
                        temp_date = temp_dates[0] + temp_dates[1] + temp_dates[2]
                        temp_date = int(temp_date)



                        self.dates.append(temp_date)
                        self.volumes.append(float(temp_volume))
                        self.close_prices.append(float(temp_close_price))
                        self.open_prices.append(float(temp_open_price))
                    except:
                        #removes top element
                        pass
        except:
            print(self.id, "ommitted from update (id not found in company_library folder)")

    def get_market_cap(self):
        path = "companylist.csv"
        try:
            with open(path,'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[0] == self.id:
                        self.market_cap = int(line[3])
                        break
        except:
            pass
    def get_change_in_price(self, start, end):
        """
        Return the change in price over the start and end dates
        :param start:
        :param end:
        :return:
        """
        if start not in self.dates or end not in self.dates:
            raise IndexError
        start_index = self.dates.index(start)
        end_index = self.dates.index(end)
        return (self.close_prices[end_index] - self.open_prices[start_index])/self.open_prices[start_index]

    def get_average_rate(self, start: int, end: int, category: str):
        """
        Return the average rate of change for a specific time-range
        start: start_date int
        end: end_date int
        category: price or volume
        """

        if start not in self.dates or end not in self.dates:
            raise IndexError

        start_index = self.dates.index(start)
        end_index = self.dates.index(end)

        if category == "PRICE":
            return (self.close_prices[start_index] +\
                    ((self.close_prices[end_index]-self.close_prices[start_index])/ \
                    (end_index-start_index)))/self.close_prices[start_index] - 1
        else:
            return (self.volumes[start_index] + \
                    ((self.volumes[end_index]-self.volumes[start_index])/\
                    (end_index-start_index)))/self.volumes[start_index] - 1

    def getavg(self, start: int, end: int, category: str):
        """
        RETURN THE AVG VOLUME/PRICE
        """
        if start not in self.dates or end not in self.dates:
            raise IndexError

        start_index = self.dates.index(start)
        end_index = self.dates.index(end)
        if category == "PRICE":
            sum = 0
            for i in range(start_index,end_index+1):
                sum += self.close_prices[i]
            sum = sum/(end_index-start_index)
            return sum
        else:
            sum = 0
            for i in range(start_index,end_index+1):
                sum += self.volumes[i]
            sum = sum/(end_index-start_index)
            return sum


    def __str__(self):
        """
        Return the ID of the company
        """
        return self.id

if __name__ == "__main__":
    start_date = 20170524
    end_date  = 20180522