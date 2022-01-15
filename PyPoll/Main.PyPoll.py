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
    votes1 = []#list of to total votes per candidate
    percentage = []#list of percentages of the total votes
    winner = ''#string name of the candidate who wont


    for row in csv_reader:
        voters.append(row['Voter ID'])#appending all the voters to the list
        votes.append(row['Candidate'])#appenfing all candidates instances to the list
        total_votes= len(voters)#calculating total of voters
        totals= len(votes)#calculating total of votes
    
    #creating the list of candidates
    for i in votes:
        if i not in candidates:
            candidates.append(i)  
    candicount= len(candidates)#calculating how many candidates are there
   
    #Counting votes and finding max min and percentage
    for j in range (0,candicount):
        name = candidates[j]
        votes1.append(votes.count(name))#adding all the votes in a list
        max_vote = max(votes1)#finding the total votes for the winner
        max_index = votes1.index(max_vote)#finding the index
        winner = candidates[max_index]# pulling the name of the winner base on the index
        vprct ="%{:.3f}".format((votes1[j]/totals)*100)#calculating percentage
        percentage.append(vprct)#appending to the list

# saving to txt file
results = open("Election_Results.txt", "w")
L1 = "Election Results"
L2 = "--------------------------"
L3 = str(f"Total Votes: {str(total_votes)}")
L4 = str("--------------------------")
results.write('{}\n{}\n{}\n{}\n'.format(L1, L2, L3, L4))#setting the formatting- and writting to the file
for i in range(len(candidates)):#looping through the candidate list
     layout = str(f"{candidates[i]}: {str(percentage[i])} ({str(votes1[i])})")
     results.write('{}\n'.format(layout))
L5 = "--------------------------"
L6 = str(f"Winner: {winner}")
L7 = "--------------------------"
results.write('{}\n{}\n{}\n'.format(L5, L6, L7))#setting the formatting- and writting to the file
results.close()

#Printing results on screen
screen = ''#String to bring the saved txt to the screen
f = open("Election_Results.txt", "r")#openninf daved tst file
for x in f:
    screen = screen + x
print(' ')
print(screen)
print("_______________________________________")   
print ("File saved as!", "Election_Results.txt")
print("_______________________________________")