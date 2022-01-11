
import csv
import os
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

candidate = ""
can_votes = {}
total_votes = 0
perc_of_candidate= {}
winner_total = 0
winner = ""

with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvReader, None)
    for row in csvReader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in can_votes:
            can_votes[candidate] = can_votes[candidate] + 1    
        else:
            can_votes[candidate] = 1   
print(can_votes)
print(votes_ct)
for name, votes_ct in can_votes.items():
    perc_of_candidate[name] = "{0:.0%}".format(votes_ct/total_votes)
    if votes_ct > winner_total:
        winner_total = votes_ct
        winner = name

print("Election Results")
print("--------------------------")
print(f" Total Votes: {total_votes}") 
print("--------------------------")
for name, votes_ct in can_votes.items():
    print(f"{name}: {perc_of_candidate[name]} ({votes_ct})")
print("--------------------------")
print(f"AND the Winner is: {winner}!")
print("--------------------------")