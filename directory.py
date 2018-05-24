from load_files import generate_company_list
from company import Company
class Directory:

    def __init__(self):
        self.companies = []
        temp_list = generate_company_list()
        for id in temp_list:
            company_name = Company(id)
            if company_name.dates != []:
                self.companies.append(company_name)
        self.top = []

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
                    temp.append(top/bottom)
                    company.append(id)


            except:

                print(id,"volume is zero at the given time")

        selectionSort(temp,company)
        print("------------------------------------------")
        for i in range(len(company)):
            print(company[i],temp[i])
        self.top = temp
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
                    temp.append(top/bottom)
                    company.append(id)


            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)
        print("------------------------------------------")
        for i in range(len(company)):
            print(company[i],temp[i])
        self.top = temp
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
                    temp.append(top/bottom)
                    company.append(id)


            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)
        print("------------------------------------------")
        for i in range(len(company)):
            print(company[i],temp[i])
        self.top = temp
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
                    temp.append(top/bottom)
                    company.append(id)

            except:
                print(id, "volume is zero at the given time")

        selectionSort(temp,company)
        print("------------------------------------------")
        for i in range(len(company)):
            print(company[i],temp[i])
        self.top = temp
        return (company,temp)

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
    start_date = 20170523
    end_date = 20180522

    all_companies.generate_zoneA(start_date,end_date,.009)
    all_companies.generate_zoneD(start_date,end_date,.009)

