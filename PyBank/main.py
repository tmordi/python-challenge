import os
import csv

csvpath = os.path.join("resources","budget_data.csv")

with open('budget_data.csv', 'r') as file:
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
    




