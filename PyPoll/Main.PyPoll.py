# First we'll import the os module
# Module to open file paths across operating systems
import os

# Module for reading CSV files
import csv
from typing import Counter

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    voters = []#list of all voters
    votes = []#list of all votes
    candidates = []#list of candidates
    votes1 = []
    percentage = []
    index = 100
    for row in csv_reader:
        voters.append(row['Voter ID'])#reading all rows under the header "Date" & adding to the list
        votes.append(row['Candidate'])#reading all rows under the header "Profit/Losses" & adding to the list
        total_votes= len(voters)# total months is equal to lenght of list "dates"
        totals= len(votes)
        index += 1
        if index == Counter:
            break
    for i in votes:
        if i not in candidates:
            candidates.append(i)  
    candicount= len(candidates)
    for j in range (0,candicount):
        name = candidates[j]
        votes1.append(votes.count(name))
        max_vote = max(votes1)
        max_index = votes1.index(max_vote)
        #  vprct = votes1[j]/totals
        #  percentage.append(vprct)
    print(candidates)
    print(votes1)
    print(max_vote)
    
        #"${}".format(sum(total))#totals is equal to the sum of the list "total"

#     for i in range(months-1):
#         bfr_idx=int(total[i])#set the index for subtrahend
#         afr_idx=int(total[(i+1)])#set the indes for minuend
#         delta.append(afr_idx-bfr_idx)#set the difference & adding to the list
#         average = "${:.2f}".format(sum(delta)/len(delta))#calculates the average of the diferences
#         Max = "${}".format(max (delta))#finding th max within the delta list
#         Min = "${}".format(min (delta))#finding th min within the delta list

# #printing results on screen
# results = (
#     f"Financial Analysis\n"
#     f"----------------------------------\n"
#     f"Total Months: {months}\n"
#     f"Total: {totals}\n"
#     f"Average Change: {average}\n"
#     f"Greatest Increase in Profits: ({Max})\n"
#     f"Greatest Decrease in Profits: ({Min})")

# print (" ")
# print (results)

# #saving results to a .txt file
# with open("../PyBank/Financial_Analysis.txt", "w") as txt_file:
#     txt_file.write(results)
# print("-----------")   
# print ("File saved as!", "Financial_Analysis.txt")
# print("-----------")
