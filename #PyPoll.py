<<<<<<< HEAD
#PyPoll
#The Data we need to retrieve.
#1.The total number of votes cast
#2. A Complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on poular vote.

#Import the datetime class from the datetime module.
import datetime
#Use the (now) attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#print the present time.
print("The time right now is", now)
import csv
dir(csv)

#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.


#To do: perform analysis.
print(election_data)

#Close the file.
election_data.close()

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Winnign Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Print the file object.
    print(election_data)

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we write data to the file.
open(file_to_save, "w")

#Using the with statement open file as a text file.
with open(file_to_save, "w") as txt_file:
    
    #write these three counties to file.
    txt_file.write("Counties in the election\nArapahoe\nDenver\nJefferson")
    
 #Add our dependencies.
import csv
import os

 #Assign a variable to a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") 

#Assign a variable to save the file to  apath.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:

    # 2. Add to the toal vote count.
        total_votes += 1

    #Print the candidate name from each row
    candidate_name = row[2]

    # If the candidate does not match any exsisting candidates...
    if candidate_name not in candidate_options:
    
      #Add it to the list of candidates
      candidate_options.append(candidate_name)

      #Begin tracking the candidate's vote count.
      candidate_votes[candidate_name] = 0

      #Add a vote to that candidate's count.
      candidate_votes[candidate_name] += 1

    #Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #4.To Do: Print out each candidate's name, vote count, and percentage of votes in terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Determine winning vote count and candidate
#1. Determine if the voters are greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning _percentage):
    #2. If true the set winning_count = votes and winning_percent = vote_ percent
    winning_count = votes
    winning_percentage = vote_percentage
    #3. Set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------\n
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------\n"
    )
#TO Do: print out the winning candidate, vote count and percentage to terminal.
print(winning_candidate_summary)
=======
#PyPoll
#The Data we need to retrieve.
#1.The total number of votes cast
#2. A Complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on poular vote.

#Import the datetime class from the datetime module.
import datetime
#Use the (now) attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#print the present time.
import csv
dir(csv)

#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
election_data = open(file_to_load, 'r')
#or for no need to open or close use:   with ope(file_to load) as election_data:

#To do: perform analysis.
print(election_data)

#Close the file.
election_data.close()

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Print the file object.
    print(election_data)

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we write data to the file.
open(file_to_save, "w")

#Using the with statement open file as a text file.
with open(file_to_save, "w") as txt_file:
    
    #write these three counties to file.
    txt_file.write("Counties in the election\nArapahoe\nDenver\nJefferson")
    
 #Add our dependencies.
import csv
import os
 #Assign a variable to a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") 
#Assign a variable to save the file to  apath.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row.
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
>>>>>>> b5c7741cd50f65f8f292b28e8c8e4e00b153a33f
