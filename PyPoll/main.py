import os
import csv

#bring in csv file
election_data = os.path.join("Resources", "election_data.csv")

#create list of output statements
output = []

#read csv file
with open(os.path.abspath(election_data)) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #create lists to hold votes and candidates
    votes = []
    candidates = []
    
    skip_head = 1

    #counts votes
    for row in csvreader:
        if skip_head:
            skip_head = 0
        else:
            votes.append(row)
            
    row_count = len(votes)

    #finds unique candidate names
    for row in votes:
        candidate = row[2]
        if candidate not in candidates: 
            candidates.append(candidate) 
    
    #print statments
    output.append('Election Results')
    output.append("-------------------------")
    output.append(f'Total Votes: {row_count}')
    output.append("-------------------------")

    #create variable to hold winner
    winner = ""
    max_votes = 0

    #calculates votes per candidate and percentage of votes
    for candidate in candidates:
        total_votes = 0
        for row in votes:
            if row[2] == candidate:
                total_votes += 1
        if total_votes > max_votes:
            max_votes = total_votes
            winner = candidate
        percentage = total_votes/row_count*100
        output.append(f'{candidate}: {percentage:.3f}% ({total_votes})')

    #print statements
    output.append("-------------------------")
    output.append(f'Winner: {winner}')
    output.append("-------------------------")

    #output to text file
    with open ("output.txt","w") as f:
        f.writelines(output)
    #output to terminal
    for line in output: 
        print(line)