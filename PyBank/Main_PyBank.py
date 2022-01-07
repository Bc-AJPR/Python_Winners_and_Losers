# First we'll import the os module
# Module to open file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    dates = []
    total = []
    delta = []

    for row in csv_reader:
        dates.append(row['Date'])
        total.append(int(row['Profit/Losses']))
        months= len(dates)
        totals= sum(total)
        
    for i in range(months):
        print(months)
        delta.append((i+1)-i)
    print(delta)
    Max = max(delta)

print( )
print("Financial Analysis" )
print("-------------------------------------")
print("Total Months:", months)
print("Total:", totals)
print("Average Change:", totals)
print("Greatest Increase in Profits:", Max)
print("Greatest Decrease in Profits:", totals)