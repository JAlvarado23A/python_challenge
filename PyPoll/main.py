#Dependencies
import os
import csv

#Specify my reading file
csv_path = os.path.join("..", "Resources", "03-Python_hw_Instructions_PyPoll_Resources_PyPoll_Resources_election_data (1).csv")

#create handler and read file
with open(csv_path, newline='', encoding = 'latin1') as csvfile:
	poll_csv_reader = csv.reader(csvfile, delimiter = ',')

	#read and skip the header
	csv_header = next(poll_csv_reader)

#read through entire file and collect candidate names (can use length of this list for total votes too)
	names = []
	for row in poll_csv_reader:
		names.append(row[2])

	#set unique name to list to identify total counts
	cand_names = list(set(names))
	
	# "reset" the csv list to the first line & skip header
	csvfile.seek(0)
	csv_header = next(poll_csv_reader)

	#ran the print to find out how many unique candidates there are and begin my counter(no need to run again)
	#print(len(cand_names))

	#Run through the csv once again to gather total count of each candiate 
	votes = [0, 0, 0, 0]
	for row in poll_csv_reader:
		if row[2] == cand_names[0]:
			votes[0] += 1
		elif row[2] == cand_names[1]:
			votes[1] += 1
		elif row[2] == cand_names[2]:
			votes[2] += 1
		elif row[2] == cand_names[3]:
			votes[3] += 1

	#calculate percentages. First store length of names as a variable (total)
	total_votes = len(names)

	percent_votes = []
	for num in votes:
		temp_percent = round((num/total_votes) * 100, 2)
		percent_votes.append(temp_percent) 


#identify winner
wvotes = 0
for i in range(0, len(cand_names)-1, 1):
	if votes[i] > wvotes:
		wvotes = votes[i]
		winner = cand_names[i]



#--------------------------------------------------------------------------------------------------
# Print Results to turminal
#--------------------------------------------------------------------------------------------------
print(f"Election Results")
print(f"----------------------------------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------------------------------------------------------------")
for i in range(len(cand_names)):
	candidate_name = str(cand_names[i])
	candidate_perc = str(percent_votes[i])
	candidate_votes = str(votes[i])

	print(f"{candidate_name}: {candidate_perc}% ({candidate_votes})")

print(f"----------------------------------------------------------------------------------")
print(f"Winner: {winner}")
print(f"----------------------------------------------------------------------------------")


#--------------------------------------------------------------------------------------------------
# Print Results as text file
#--------------------------------------------------------------------------------------------------
data_output = os.path.join("..", "Analysis", "Poll_Analysis.txt")
with open(data_output, "w") as txtfile:
	writer = csv.writer(txtfile)

	writer.writerow([f"Election Results"])
	writer.writerow([f"----------------------------------------------------------------------------------"])
	writer.writerow([f"Total Votes: {total_votes}"])
	writer.writerow([f"----------------------------------------------------------------------------------"])
	for i in range(len(cand_names)):
		candidate_name = str(cand_names[i])
		candidate_perc = str(percent_votes[i])
		candidate_votes = str(votes[i])

		writer.writerow([f"{candidate_name}: {candidate_perc}% ({candidate_votes})"])

	writer.writerow([f"----------------------------------------------------------------------------------"])
	writer.writerow([f"Winner: {winner}"])
	writer.writerow([f"----------------------------------------------------------------------------------"])