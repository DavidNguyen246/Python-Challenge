# import the csv and as modules
import csv
import os

# load the file to read the survey data
inputFile = os.path.join("resources", "election_data.csv")

# output file location for the election data analysis
outputFile = os.path.join("Analysis", "ElectionDataAnalysis.txt")

# variables
totalVotes = 0      # variable that holds the total number of votes
candidates = []     # list that holds the candidate in election
candidateVotes = {} # dictionary that will hold the votes each candidate receives  
winningCount = 0 # variable hold the winning count
winningCandidate = "" # a variable to hold the winning candidate

# read the csv file
with open(inputFile) as electionData:
    #create the csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    #row will be lists
        # index 0 is the Ballot ID
        # index 1 is the country

    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1

        # check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # if the candidate is not in the list, add the candidate to list of candidates
            candidates.append(row[2])

            # add the value to the dictionary as well
            # { "key": value }
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1
        
        else:
            # the candidate is in the list of candidates
            # add a vote to the candidate's count
            candidateVotes[row[2]] += 1

#print(candidatevotes)
voteOutput = ""
for candidate in candidateVotes:
    # get the vote count and the percentage of the votes
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100.00
    voteOutput += f"{candidate}: {votePct:.3f}% ({votes:,})\n"

    # compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winning count
        winningCount = votes
        # update the winning candidate
        winningCandidate = candidate

winningCandidateOutput = f"Winner: {winningCandidate}\n-------------------------------"



# create an output variable to hold the output
output = (
    f"\n\nElection Results\n"
    f"-------------------------------\n"
    f"Total Votes: {totalVotes:,}\n-------------------------------"  
    f"\n{voteOutput}-------------------------------"
    f"\n{winningCandidateOutput}"
)

# display output to the console 
print(output)

# print the results and export the data to a text file
with open(outputFile, "w") as textFile:
    # write the output to the text file
    textFile.write(output)