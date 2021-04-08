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

	