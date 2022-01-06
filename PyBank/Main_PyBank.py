# First we'll import the os module
# Module to open file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    #csv_reader. next() #to skip the header
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    #print(csv_reader)
    lines= len(list(csv_reader))
    numbers = (float(row[1]) for row in csv_reader)
    total = sum(numbers)
    print( )
    print("Financial Analysis" )
    print("-------------------------------------")
    print("Total Months:", lines)
    print("Average Change:", total)
    print("Greatest Increase in Profits:", lines-1)
    print("Greatest Decrease in Profits:", lines-1)