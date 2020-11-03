# The data we need to retrieve
# The total number of votes cast
# List of the candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of election based on popular votes

# Assign a variable to file to load and path
file_to_load='Resources\election_results.csv'
# open the election rsults and read the file
with open (file_to_load) as election_data:
# To do: Perform analysis
    print (election_data)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join ("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join ("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter
total_votes=0
# Open the election results and read the file.
with open (file_to_load) as election_data:
    # to do analysis here
#read the file object with the reader function
    file_reader = csv.reader(election_data)
# Read and print the header row
    headers=next(file_reader)
# print each row in the csv file
    for row in file_reader:
    # 2. Add to the total votes count
        total_votes += 1  
# 3. Print the Total Votes
print(total_votes)



