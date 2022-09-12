#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filemane variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total_votes to zero.
total_votes=0
#candiate options and candidate votes
candidate_options=[]
#decalre empty dictionary.
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count=0
winning_percentage=0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row.
    headers=next(file_reader)

    #1. Print the total number of votes cast
    for row in file_reader:

        #add to the total vote count.
        total_votes +=1

        #2. print the candidate name from each row
        candidate_name = row[2]


        #If then candiate does not match any existing candidate..
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1

        #determine the percentage of votes for each candidate by loopingg through the counts.
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # retrieve vote count of a candidate
            votes= candidate_votes[candidate_name]
            #calculate the percentage of votes
            vote_percentage=float(votes)/float(total_votes)*100
            
            #print the candidate name and percentage of votes
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #determine winning vote count and candidate
            
            #determine if the votes are greater than the winning count.
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name
        winning_candidate_summary=(
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------\n")
        print(winning_candidate_summary)
