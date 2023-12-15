# Import os and csv
import csv
import os

# Load file  to read election_data.csv
inputFile = os.path.join("Resources\election_data.csv")

# Load file output to a text file (analysis)
outfile = os.path.join("analysis.text")

# Variables
# Holds the value of number of votes...adding one
totalVotes = 0
# Holds the all candidates in election
candidates =[]
# Holds the number votes for each candidates in dictionary
candidatesVotes = {}
#Track winning candidate
winningCount = 0
winningCandidate = "" 

# Read the csv file
with open (inputFile) as electionData:
    # Create the csv reader
    csvreader = csv.reader(electionData)

    # Read in header
    header = next(csvreader)

    # Row will be list
        # index 0 is Ballot ID
        # index 1 is County
        # index 2 is Candidate
    
    # For each row
    for row in csvreader:
        # add total votes to totalVotes...adding by one
        totalVotes += 1


        # check to if the candidte is in the list of candidates
        if row[2] not in candidates:
            # if candidates not in list add (append) candidate to list
            candidates.append(row[2])

            # add value to dictionary [key[value]]
            #add a vote to the candidate count...will start with one
            candidatesVotes[row[2]] = 1

        else:
            # The canidadte is in the list so just count the vote
            candidatesVotes[row[2]] += 1
#print(candidatesVotes) #print to check counts and dictionary
voteOutput =""         
for candidates in candidatesVotes:
            # Gettting vote count and percent of the votes
            votes = candidatesVotes.get(candidates)
            # value of vote precnt
            votePrecent = (float(votes)/ float(totalVotes)) * 100.00
           # print(votes) # Print to check values are correct
            voteOutput += f"\n{candidates}: {votePrecent:.3f}%: ({votes}) \n"
            #print(voteOutput) print to check for correct output


            # compare candidates with highest votes
            if votes > winningCount:
                 #update the votes to winning count
                 winningCount = votes
                 #Update the winning candidate
                 winningCandidate = candidates

#print winning candidate
                 winningCandidateOutput = f"Winner: {winningCandidate}"

            

# Create an output variable to hold output
output =(
    f"\n Election Results\n\n"
    f"-------------------------\n\n"
    f"Total Votes: {totalVotes:,}\n\n"
    f"-------------------------\n\n"
    f"{voteOutput}"
    f"\n\n-------------------------\n\n"
    f"{winningCandidateOutput}\n\n"
    f"-------------------------\n\n"
)
# Display out to termal
print(output)


# Disply output tp a text file (anaylsis)
with open(outfile, "w") as texFile:
    # write to text file
    texFile.write(output)