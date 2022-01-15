# Modules
from fileinput import close
import os
import csv
from typing import Counter

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    voters = []#list of all voters
    votes = []#list of all votes
    candidates = []#list of candidates
    votes1 = []
    percentage = []
    overall = {}


    for row in csv_reader:
        voters.append(row['Voter ID'])#reading all rows under the header "Date" & adding to the list
        votes.append(row['Candidate'])#reading all rows under the header "Profit/Losses" & adding to the list
        total_votes= len(voters)# total months is equal to lenght of list "dates"
        totals= len(votes)
    for i in votes:
        if i not in candidates:
            candidates.append(i)  
    
    candicount= len(candidates)
    for j in range (0,candicount):
        name = candidates[j]
        votes1.append(votes.count(name))
        max_vote = max(votes1)
        max_index = votes1.index(max_vote)
        winner = candidates[max_index]
        vprct ="%{:.3f}".format((votes1[j]/totals)*100)
        percentage.append(vprct)

# # Results
# print(" ")
# print("Election Results")
# print("--------------------------")
# print(f"Total Votes: {str(total_votes)}")
# print("--------------------------")
# for i in range(len(candidates)):
#     print(f"{candidates[i]}: {str(percentage[i])} ({str(votes1[i])})")  
# print("--------------------------")
# print(f"Winner: {winner}")
# print("--------------------------")

#saving results to a Election_Results.txt file
results = open("Election_Results.txt", "w")
L1 = "Election Results"
L2 = "--------------------------"
L3 = str(f"Total Votes: {str(total_votes)}")
L4 = str("--------------------------")
results.write('{}\n{}\n{}\n{}\n'.format(L1, L2, L3, L4))
for i in range(len(candidates)):
     layout = str(f"{candidates[i]}: {str(percentage[i])} ({str(votes1[i])})")
     results.write('{}\n'.format(layout))
L5 = "--------------------------"
L6 = str(f"Winner: {winner}")
L7 = "--------------------------"
results.write('{}\n{}\n{}\n'.format(L5, L6, L7))
results.close()

#Printing results on screen
f = open("Election_Results.txt", "r")
for x in f:
  print(x)
print("_______________________________________")   
print ("File saved as!", "Election_Results.txt")
print("_______________________________________")