import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = list(reader)

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = 0
greatest_decrease = 0

# Iterate through the data to calculate the required values
for i in range(len(data)):
    total_months += 1
    net_total += int(data[i][1])
    if i > 0:
        change = int(data[i][1]) - int(data[i-1][1])
        changes.append(change)
        
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = data[i][0]
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = data[i][0]

average_change = sum(changes) / len(changes)

# Print the analysis results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")




