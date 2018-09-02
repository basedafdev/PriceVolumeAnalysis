from directory import Directory
from company import Company
from directory import selectionSort
def probability_of_returns(og_date, directory):
    temp = Company('GOOG')
    date = temp.dates.index(og_date)
    next_date = date+8
    results = directory.get_reversals_up(og_date)
    selectionSort(results[1], results[0],1)
    results = results[0]
    print(len(results))
    probability = 0
    for company in results:
        change = 0

        change = company.get_average_rate(company.dates[date],company.dates[next_date],"PRICE")
        print(company, change)

        if change < 0:
            probability += 1

    probability /= len(results)
    print(probability)
def gains(og_date, directory):
    pass
if __name__  == "__main__":
    x = Directory()
    probability_of_returns(20180618,x)
    probability_of_returns(20180619,x)
    probability_of_returns(20180620,x)
