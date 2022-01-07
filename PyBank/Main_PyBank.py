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
        totals= "${:,.2f}".format(sum(total))
    #print (total[i]) for i in range(len(dates))])
    for i in range(months-1):
        bfr_idx=int(total[i])
        afr_idx=int(total[(i+1)])
        delta.append(afr_idx-bfr_idx)
        average = "${:,.2f}".format(sum(delta)/months)
        Max = "${:,.2f}".format(max (delta))
        Min = "${:,.2f}".format(min (delta))

print( )
print("Financial Analysis" )
print("-------------------------------------")
print("Total Months:", months)
print("Total:", totals)
print("Average Change:", average)
print("Greatest Increase in Profits:", Max)
print("Greatest Decrease in Profits:", Min)