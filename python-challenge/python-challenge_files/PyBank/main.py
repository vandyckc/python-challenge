import csv
import os

# read in csv file
with open('budget_data.csv', 'r') as budget_data:
    csvreader = csv.DictReader(budget_data, delimiter=',')

    budget_data = []
    for row in csvreader:
        budget_data.append(row)

 # total profit/losses
    total_net = sum(int(row['Profit/Losses']) for row in budget_data)

    print('Total Profit/Losses:', total_net)

# total months
    total_months = len(budget_data)
    print(total_months)

# net change
    NumList = []
    DateList = []
    for row in budget_data:
        if len(row.keys()) > 1:
            try:
                num = int(row['Profit/Losses'])
                NumList.append(num)
                date = row['Date']
                DateList.append(date)
            except ValueError:
                pass

    PointChange = []
    for index, value in enumerate(NumList):
        try:
            value2 = NumList[index + 1]
            change = value2 - value
            PointChange.append(change)
        except:
            pass

    DayChange = dict(zip(DateList[1:], PointChange))
    print(DayChange)

# calculate max
    max_profit = max(PointChange)
    print(max_profit)

# calculate min
    min_profit = min(PointChange)
    print(min_profit)

# average change

    avg_change= sum(PointChange)/len(PointChange)
    print(avg_change)
# output script as text file
def script_txt(budget_practice):
    with open(budget_practice) as f:
        data = f.read()
        f.close()

    with open("PyBank_script.txt", mode="w") as f:
        f.write(data)
        f.close()

script_txt("budget_practice.ipynb")
