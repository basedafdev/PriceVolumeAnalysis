from load_files import generate_company_list
from company import Company
import smtplib
import csv
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
        self.invested_top_five = []
        self.zoneA = []


        temp_list = generate_company_list()
        temp_list = list(set(temp_list))
        for id in temp_list:
            try:
                company_name = Company(id)
                if company_name.dates != []:
                    self.companies.append(company_name)
            except:
                pass

    def generate_zoneA(self,start,end):
        """
        Return a list of all the increasing companies in zone A
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
        return (company[-5:],temp[-5:])

    def generate_top_longterm(self):
        """
        Returns the best long-term stocks to invest in

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
        return (company[-5:],temp[-5:])


    def get_reversals_up_ui(self, max_price_change, max_price, volume,date):
        temp = []
        company = []

        for id in self.companies:
            try:

                day_of_trade = 0
                day_before = 0
                if date not in id.dates:
                    day_of_trade = len(id.dates)

                else:
                    day_of_trade = id.dates.index(date)
                day_before = day_of_trade - 1
                price_change = id.get_average_rate(id.dates[day_before - 1], id.dates[day_before], "PRICE")

                historical_volume = id.getavg(id.dates[day_before - 15], id.dates[day_before - 1], "VOLUME")

                today_price = id.close_prices[day_before]
                today_volume = id.volumes[day_before]
                yesterday_volume = id.volumes[day_before - 1]
                if 0 < price_change < max_price_change and max_price > float(today_price) > 2 and historical_volume > volume\
                        and today_volume > yesterday_volume:
                    temp.append((today_volume - historical_volume) / historical_volume)
                    company.append(id)
            except:
                pass

        selectionSort(temp, company)
        return (company[-5:], temp[-5:])
    def get_reversals_up(self, date):
        """
        Returns a list of potential up-ward reversals
        1) If the price from yesterday rose today
        2) if the toady's price is > 2
        3) if today's volume is greater than the historical volume
        4) price_change * today's volume / historical volume
        """
        temp = []
        company = []

        for id in self.companies:
            try:

                day_of_trade = 0
                day_before = 0
                if date not in id.dates:
                    day_of_trade = len(id.dates)

                else:
                    day_of_trade = id.dates.index(date)
                day_before = day_of_trade-1
                price_change = id.get_average_rate(id.dates[day_before-1], id.dates[day_before] , "PRICE")

                historical_volume = id.getavg(id.dates[day_before-10], id.dates[day_before-1], "VOLUME")

                today_price = id.close_prices[day_before]
                today_volume = id.volumes[day_before]
                yesterday_volume = id.volumes[day_before-1]
                if 0 < price_change < 0.1 and 150 > float(today_price) > 5 and historical_volume > 100000 and \
                        today_volume > historical_volume and today_volume > yesterday_volume        :
                    temp.append((today_volume-historical_volume)/historical_volume)
                    company.append(id)
            except:
                pass

        selectionSort(temp, company)
        return (company[-10:], temp[-10:])

    def gains(self, start1, end1):
        """
        REturn the returns of a certian stock from the start day you invested to the end

        """
        sum = 0
        companies = self.get_reversals_up(start1)
        for company in range(len(companies[0])):
            start = companies[0][company].dates.index(start1)
            end = companies[0][company].dates.index(end1)
            run = True
            the_company = companies[0][company]
            if run:
                for i in range(start,end+1):
                    if the_company.volumes[start] < the_company.volumes[i] and the_company.close_prices[i] < the_company.close_prices[i-1]:
                    #if the_company.close_prices[start] - the_company.close_prices[i] > 2*the_company.get_true_range(start1,10):
                        sum += the_company.get_change_in_price(start1, companies[0][company].dates[i])*20000 +(20000)

                        print(the_company,the_company.get_change_in_price(start1, the_company.dates[i]))
                        print("SOLD WHEN PRICE CHANGE is 2 TR's Away: ", the_company.dates[i])

                        run = False
                        break

            if run:
                print(the_company,the_company.get_change_in_price(start1, end1))
                sum += the_company.get_change_in_price(start1, end1) *20000 + (20000)

        print("Day's Returns:", sum, "|| PERCENT RETURN", str((sum - 100000) / 100000))
        print("________________________________________")

        return (sum - 100000) / 100000

    def overall_gains1(self, start1, end1):
        total = 0

        x = Company('GOOG')
        today_date = x.dates[len(x.dates)-1]
        start = x.dates.index(start1)
        end = x.dates.index(end1)
        for i in range(start, end + 1):
            total += self.gains(x.dates[i], end1)
        return total

    def overall_gains(self, start1, end1):
        """
        Generates a csv document of all the potential gains from
        a certain company
        """

        all_companies = []
        company_names = []

        dates = []
        x = Company('GOOG')
        start = x.dates.index(start1)
        end = x.dates.index(end1)
        for i in range(start,end+1):
            for company in self.get_reversals_up(x.dates[i])[0]:

                all_companies.append((company,x.dates[i]))

        #Sort company alphabetically
        for i in all_companies:
            company_names.append(str(i[0]))
        alpha_sort(company_names, all_companies)

        sum = 0
        for i in range(len(all_companies)):
            try:
                b = all_companies[i][0].get_change_in_price(all_companies[i][1],end1)
                if b < -.1:
                    sum += -.1
                    print(all_companies[i][0], "-.1",
                          all_companies[i][1])
                else:
                    sum += b
                    print(all_companies[i][0], all_companies[i][0].get_change_in_price(all_companies[i][1],end1), all_companies[i][1])
            except:
                pass

        print(sum)
    def short_sell(self,date):
        """
        Returns a list of potential down-ward reversals. Perfect for them short sellers
        1)
        2)
        3)
        4)
        """

        temp = []
        company = []

        for id in self.companies:
            try:

                day_of_trade = 0
                day_before = 0
                if date not in id.dates:
                    day_of_trade = len(id.dates)

                else:
                    day_of_trade = id.dates.index(date)
                day_before = day_of_trade - 1
                price_change = id.get_average_rate(id.dates[day_before - 1], id.dates[day_before], "PRICE")

                historical_volume = id.getavg(id.dates[day_before - 22], id.dates[day_before - 1], "VOLUME")

                today_price = id.close_prices[day_before]
                today_volume = id.volumes[day_before]
                if 0 < price_change < -0.05 and float(today_price) > 2 and historical_volume > 100000:
                    temp.append((today_volume - historical_volume) / historical_volume)
                    company.append(id)
            except:
                pass

        selectionSort(temp, company)
        return (company[-5:], temp[-5:])
    def get_zone(self, company, start_date, end_date):
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

def alpha_sort(alist,company):
    """
    SOrt thigns alphabetically
    :param alist:
    :param company:
    :return:
    """
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if str(alist[location]) > str(alist[positionOfMax]):
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        temp1 = company[fillslot]
        company[fillslot] = company[positionOfMax]
        company[positionOfMax] = temp1
def sendmail(s,subject,email_list):
    """
    Connects the built in email python library
    and sends an email to given emails in the email_list

    """

    SUBJECT = subject
    message = 'Subject: {}\n\n{}'.format(SUBJECT, s)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('applicationtestemail123@gmail.com', 'langlaile@1')
    for email in email_list:
        mail.sendmail('fromemail', email, message)
    mail.close()

if __name__ == "__main__":
    """
    MAIN METHOD
    PASS IN A DATE TO RETURN THE TOP 10 STOCKS TO INVEST IN
    THAT DAY 
    """

    all_companies = Directory()
    print("________________")
    s = ""
    date = ""
    while date != 0:
        date = int(input("Enter the date you want to know: "))
        s+= str(date) + "\n"
        out = all_companies.get_reversals_up(date)
        for i in range(len(out[0])):
            s += str(10-i) + ") " + str(out[0][i]) + " " + str(out[1][i]) + '\n'
        print(s)
        email_list = ["tommyliu9@gmail.com","svj5271@gmail.com","ashwin23suresh@gmail.com",
        "jjh235@scarletmail.rutgers.edu","avni.mandhania@gmail.com","adamwstephens@gmail.com",
        "djdmello15@gmail.com"]
        email_list2 = ["tommyliu9@gmail.com", "jjh235@scarletmail.rutgers.edu","tarun.mandhania@kinetixtt.com"]
        sendmail(s,"TOP 10 Potential Reversals",email_list2)
        s += "----------------------- " + "\n"
    date = 3
    while date != 0:
        start = int(input("enter start: "))
        end = int(input("enter end: "))
        sum = all_companies.overall_gains1(start,end)
        print("TOTAL RETURN: ",sum)
