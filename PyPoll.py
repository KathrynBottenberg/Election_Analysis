#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filemane variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Countries in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#close the file
print (file_to_save)

#Open the elction results and read the file.
with open(file_to_load) as election_data:



    #To do: read and perform analysis.
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #print the header row.
    headers=next(file_reader)
    print(headers)

    #1. The total number of votes cast
    #2. A complete list of candidates who received votes
    #3. The percentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular votes

    #Close the file.
    print(election_data)