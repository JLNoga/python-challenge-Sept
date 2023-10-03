#read in csv file
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #create variables
    votes = 0
    countA = 0
    countB = 0
    countC = 0
    candidates = []
    dict = {}
    #loop through rows
    for row in csvreader:
        #The total number of votes cast
        votes += 1
        candidates.append(row[2]) 

    #A complete list of candidates who received votes
    uniq_candidates = list(set(candidates))
    #create candidate variables
    vcount = len(candidates)
    
    nameA = str(uniq_candidates[0])
    nameB = str(uniq_candidates[1])
    nameC = str(uniq_candidates[2])
#The total number of votes each candidate won
    for row in candidates:
        if row == nameC:
            countC += 1
        elif row == nameB:
            countB += 1
        else:   
            countA += 1

    #The percentage of votes each candidate won
    percA = countA / vcount
    percB = countB / vcount
    percC = countC / vcount
  
    fperca = (format(percA, '.2%'))
    fpercb = (format(percB, '.2%'))
    fpercc = (format(percC, '.2%'))

    name = [nameA, nameB, nameC]
    count = [int(countA), int(countB), int(countC)]
    
    #The winner of the election based on popular vote
    winner_count = max(count)
    print(winner_count)
    if winner_count == count[0]:
        winner = name[0]
    if winner_count == count[1]:
        winner = name[1]
    if winner_count == count[2]:
        winner = name[2]
    else:
        print("error in count")
    


    #print to terminal and text file
    lines = ["Election Results", "----------------------------------", f"Total Votes: {votes}",
            "----------------------------------", f"{nameA}: {fperca} ({countA})", f"{nameB}: {fpercb} ({countB})",
            f"{nameC}: {fpercc} ({countC})", "----------------------------------", f"Winner: {winner}", 
            "----------------------------------"]
    print(*lines,sep='\n')

    txtoutput = os.path.join('Analysis', 'voter_analysis.txt')
    with open(txtoutput, 'w') as f:
        f.write('\n'.join(lines))