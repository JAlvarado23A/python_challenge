#Dependencies
import os
import csv

#Specify my reading file
csv_path = os.path.join("..", "Resources", "03-Python_hw_Instructions_PyBank_Resources_budget_data.csv")

#create handler and read file
with open(csv_path, newline='', encoding = 'latin1') as csvfile:
	bank_csv_reader = csv.reader(csvfile, delimiter = ',')

	#read and skip the header
	csv_header = next(bank_csv_reader)


	#Set variables for Total Months, Total cash,...
	month_count = 0
	profits = []
	maxVal = 0
	minVal = (-1)

#read through each row and sum the number of months
	for row in bank_csv_reader:
		profits.append(float(row[1]))
		month_count += 1
	
	#reset my file to first line & skip header
	csvfile.seek(0)
	csv_header = next(bank_csv_reader)

#create a list that holds the difference in amount of everyday profit
	diff = []
	for element in range(0, len(profits)-1, 1):
		inner_diff = (profits[element + 1] - profits[element])
		diff.append(inner_diff)

		#this will find the proffit/loss associated with the date
		if inner_diff > maxVal:
			maxVal = inner_diff
			increase_date = profits[element + 1]
		elif inner_diff < minVal:
			minVal = inner_diff
			decrease_date = profits[element + 1]
	
	#use the diff list to calculate average change
	change = sum(diff)/len(diff)


	#read through each row to identify the dates corresponding to the greates increase/deccrease
	for row in bank_csv_reader:
		if float(row[1]) == increase_date:
			greatest_inc_date = (row[0])
		elif float(row[1]) == decrease_date:
			greatest_de_date = (row[0])




'''	These will give  me the greatest increase and decrease, but not the year!
	print(f"{max(diff)}")
	print(f"Min is {min(diff)}")
	print(len(diff))
'''

	#print(maxVal)
	#print(f"Max number is {max(profits)}")

#Print to termminal 
print(f"Total Months: {month_count}")
print(f"Total: ${round(sum(profits),2)}")
print(f"Average Change: ${round(change, 2)}")
print(f"Greatest Increase in Profits: {greatest_inc_date} with ${maxVal}")
print(f"Greatest Increase in Profits: {greatest_de_date} with ${minVal}")


#write as csv
data_output = os.path.join("..", "Analysis", "Bank_Analysis.txt")
with open(data_output, "w") as txtfile:
	writer = csv.writer(txtfile)

	writer.writerow([f"Total Months: {month_count}"])
	writer.writerow([f"Total: ${round(sum(profits),2)}"])
	writer.writerow([f"Average Change: ${round(change, 2)}"])
	writer.writerow([f"Greatest Increase in Profits: {greatest_inc_date} with ${maxVal}"])
	writer.writerow([f"Greatest Increase in Profits: {greatest_de_date} with ${minVal}"])

	