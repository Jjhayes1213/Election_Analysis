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
