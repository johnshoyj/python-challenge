import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(os.path.abspath(election_data)) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    votes = []
    candidates = []
    
    skip_head = 1

    for row in csvreader:
        if skip_head:
            skip_head = 0
        else:
            votes.append(row)
            
    row_count = len(votes)

    for row in votes:
        candidate = row[2]
        if candidate not in candidates: 
            candidates.append(candidate) 
    
    print('Election Results')
    print("-------------------------")
    print(f'Total Votes: {row_count}')
    print("-------------------------")

    winner = ""
    max_votes = 0

    for candidate in candidates:
        total_votes = 0
        for row in votes:
            if row[2] == candidate:
                total_votes += 1
        if total_votes > max_votes:
            max_votes = total_votes
            winner = candidate
        percentage = total_votes/row_count*100
        print(f'{candidate}: {percentage:.3f}% ({total_votes})')

    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")