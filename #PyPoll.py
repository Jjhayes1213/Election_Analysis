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

#Track the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

      #Save the results to our text file.
      with open(file_to_save, "w") as txt_file:

          #print the final vote count to the terminal.
          election_results = (
              f"\nElection_results\n"
              f"-----------------------\n"
              f"Total Votes: {total_votes:,}"
              f"------------------------\n"
          )
          print(election_results, end="")
          #Save the final vote count to the text file.
          txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        #2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

        #4.Print out each candidate's name, vote count, and percentage of votes in terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Print each candidate, their voter count, and percentage to the terminal.
    print(candidate_results)

    #Save the candidate results to our text file.
    txt_file.write(candidate_results)

#Determine winning vote count and candidate
#1. Determine if the voters are greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
    #2. If true the set winning_count = votes and winning_percent = vote_ percent
    winning_count = votes
    #3. Set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
    
#Print the winningcandidate' results to the terminal.
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------\n"
    )
#print out the winning candidate, vote count and percentage to terminal.
print(winning_candidate_summary)

#Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)


