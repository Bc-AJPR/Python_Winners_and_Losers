# First we'll import the os module
# Module to open file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    dates = []#list of all months
    total = []#list of total amounts for each month
    delta = []#list of de differences month to month

    for row in csv_reader:
        dates.append(row['Date'])#reading all rows under the header "Date" & adding to the list
        total.append(int(row['Profit/Losses']))#reading all rows under the header "Profit/Losses" & adding to the list
        months= len(dates)# total months is equal to lenght of list "dates"
        totals= "${}".format(sum(total))#totals is equal to the sum of the list "total"

    for i in range(months-1):
        bfr_idx=int(total[i])#set the index for subtrahend
        afr_idx=int(total[(i+1)])#set the indes for minuend
        delta.append(afr_idx-bfr_idx)#set the difference & adding to the list
        average = "${:.2f}".format(sum(delta)/len(delta))#calculates the average of the diferences
        Max = "${}".format(max (delta))#finding th max within the delta list
        Min = "${}".format(min (delta))#finding th min within the delta list

#printing results on screen
results = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {months}\n"
    f"Total: {totals}\n"
    f"Average Change: {average}\n"
    f"Greatest Increase in Profits: ({Max})\n"
    f"Greatest Decrease in Profits: ({Min})")

print (" ")
print (results)

#saving results to a .txt file
with open("../PyBank/Financial_Analysis.txt", "w") as txt_file:
    txt_file.write(results)
print("-----------")   
print ("File saved as!", "Financial_Analysis.txt")
print("-----------")