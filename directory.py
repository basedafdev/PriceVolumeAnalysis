from load_files import generate_company_list
from company import Company
"""
Represents a company directory
"""
class Directory:

    def __init__(self):
        """
        Initialize a new Company Directory
        companies: list of companies

        """

        self.companies = []
        self.companystrings = []
        self.zoneA = []
        self.zoneB = []
        self.zoneC = []
        self.zoneD = []

        temp_list = generate_company_list()
        for id in temp_list:
            company_name = Company(id)
            if company_name.dates != []:
                self.companies.append(company_name)
                self.companystrings.append(id)

    def generate_zoneA(self,start,end,threshold):
        """
        Return a list of all the increasing companies in zoneA
        """
        temp = []
        company = []
        for id in self.companies:
            try:
                top = id.get_average_rate(start,end,"PRICE")
                bottom = id.get_average_rate(start,end,"VOLUME")
                if top > 0 and bottom > 0:
                    temp.append(top*bottom)
                    company.append(id)


            except:

                print(id,"volume is zero at the given time")

        selectionSort(temp,company)
        for i in temp:
            print(i)
        self.zoneA = company
        return (company,temp)

    def generate_zoneB(self,start,end,threshold):
        """
        Return a list of all the increasing companies in zoneB
        """
        temp = []
        company = []
        for id in self.companies:
            try:
                top = id.get_average_rate(start,end,"PRICE")
                bottom = id.get_average_rate(start,end,"VOLUME")
                if top > 0 and bottom < 0:
                    temp.append(top*bottom)
                    company.append(id)


            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)
        self.zoneB = company
        return (company,temp)

    def generate_zoneC(self,start,end,threshold):
        """
        Return a list of all the increasing companies in zoneC
        """
        temp = []
        company = []
        for id in self.companies:
            try:
                top = id.get_average_rate(start,end,"PRICE")
                bottom = id.get_average_rate(start,end,"VOLUME")
                if top < 0 and bottom < 0:
                    temp.append(top*bottom)
                    company.append(id)


            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)
        self.zoneC = company
        return (company,temp)

    def generate_zoneD(self,start,end,threshold):
        """
        Return a list of all the increasing companies in zoneD
        """
        temp = []
        company = []
        for id in self.companies:
            try:
                top = id.get_average_rate(start,end,"PRICE")
                bottom = id.get_average_rate(start,end,"VOLUME")
                if top < 0 and bottom > 0:
                    temp.append(top*bottom)
                    company.append(id)

            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)

        self.zoneD = company
        return (company,temp)

    def get_zone(self, company: "Company", start_date: int, end_date: int):
        """
        Returns a tuple of what zone, area of growth, change in volume, and change in price.
        """
        price_change = company.get_average_rate(start_date,end_date,"PRICE")
        volume_change = company.get_average_rate(start_date,end_date,"VOLUME")
        zone = None
        if price_change > 0 and volume_change > 0:
            zone = 'A'
        elif price_change > 0 and volume_change < 0:
            zone = 'B'
        elif price_change < 0 and volume_change < 0:
            zone = 'C'
        elif price_change < 0 and volume_change > 0:
            zone = 'D'
        return (company,zone,price_change*volume_change,price_change,volume_change)

def selectionSort(alist,company):
    # Modified version of selection sort such that it supports the Company Object
    # Returns None
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       temp1 = company[fillslot]
       company[fillslot] = company[positionOfMax]
       company[positionOfMax] = temp1

if __name__ == "__main__":
    all_companies = Directory()
    start_date = 20170526
    end_date = 20180525
