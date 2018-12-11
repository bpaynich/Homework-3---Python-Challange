import os
import csv

#Arrays
list_id = []
list_country = []
list_canidate = []
unique_canidate = []
unique_vote_count = []
temp_vote_count = 0

# Setup connection to csv data file
csvpath = os.path.join('', 'Resources', '03-Python_Homework_PyPoll_Resources_election_data.csv')

# Open Data file and read into arrays
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        list_id.append(row[0])
        list_country.append(row[1])
        list_canidate.append(row[2])

    # Total Vote Count
    voter_count = len(list_id)
 
    # Get list of unique Canidates
    for x in list_canidate:
        if (x) not in unique_canidate:
            unique_canidate.append(x)
   
    # Election output header
    print ("\n")
    print ("  Election Results")
    print ("  --------------------------")   
    print ("  Total Votes: " + str(voter_count))
    print ("  --------------------------")

    # Count votes per canidate, percentage of vote, and determine winner
    for canidate in unique_canidate:
        canidate_count = list_canidate.count(canidate)
        percentage_vote = round((canidate_count / voter_count * 100), 3)
        print ("  " + canidate + ": " + str(percentage_vote) + "% (" + str(canidate_count) + ")")

        if(canidate_count > temp_vote_count):
            winner = canidate
            temp_vote_count = canidate_count
    
    print ("  --------------------------")
    print ("  Winner: " + winner)
    print ("  --------------------------")

# save the output file path
output_file = os.path.join("pypoll_output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["  Election Results"])
    writer.writerow(["  --------------------------"])
    writer.writerow(["  Total Votes: " ,str(voter_count)])
    writer.writerow(["  --------------------------"])
    writer.writerow(["  Winner: " , str(winner)])
    writer.writerow(["  ---------------------------"])