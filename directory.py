from load_files import generate_company_list
from company import Company
import smtplib

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
        temp_list = list(set(temp_list))
        for id in temp_list:
            company_name = Company(id)
            if company_name.dates != []:
                self.companies.append(company_name)
                self.companystrings.append(id)

    def generate_zoneA(self,start,end):
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
        self.zoneA = company
        return (company[-10:],temp[-10:])
    def generate_top_longterm(self):
        """

        """
        temp = []
        company = []
        for id in self.companies:
            try:
                start = id.dates[0]
                end = id.dates[len(id.dates)-1]
                top = id.get_average_rate(start, end, "PRICE")
                bottom = id.get_average_rate(start, end, "VOLUME")
                top1 = id.getavg(start, end, "PRICE")
                bot1 = id.getavg(start, end, "VOLUME")
                if top > 0 and bottom > 0:
                    temp.append(top1*bot1)
                    company.append(id)
            except:
                pass

        selectionSort(temp,company)
        return (company[-20:],temp[-20:])
    def get_reversals(self):
        pass
    def generate_top_shortterm(self):
        """

        """
        temp = []
        companies = []

        for id in self.companies:


            try:
                zone_longterm = self.get_zone(id, id.dates[0], id.dates[len(id.dates) - 1])[1]

                time_frame = id.dates[-5:]

                start_date = time_frame[0]
                end_date = time_frame[1]
                top = id.get_average_rate(start_date, end_date, "PRICE")
                bot = id.get_average_rate(start_date, end_date, "VOLUME")
                if top > 0 and (bot > 0  or bot < 0) and zone_longterm == "A":

                    companies.append(id)
                    temp.appnd(abs(top/bot))
            except:
                pass
        selectionSort(temp,companies)
        return companies[-5:]

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
def sendmail(s,email):
    x = Company("GOOG")
    SUBJECT = "TOP 10 STOCKS TO BUY (based on " + str(x.dates[len(x.dates)-1]) + ")"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, s)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('applicationtestemail123@gmail.com', 'langlaile@1')
    mail.sendmail('fromemail', email, message)
    mail.close()
if __name__ == "__main__":

    all_companies = Directory()
    print("________________")
    s = ""

    out = all_companies.generate_top_longterm()[0]
    for i in range(len(out)):
        s += str(20-i) + ") " + str(out[i]) + '\n'
    print(s)
    email_list = ["tommyliu9@gmail.com","svj5271@gmail.com","ashwin23suresh@gmail.com",
                  "jjh235@scarletmail.rutgers.edu","avni.mandhania@gmail.com","adamwstephens@gmail.com",
                  "djdmello15@gmail.com"]
    for i in email_list:
        sendmail(s,i)