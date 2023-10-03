# Import os
import os
# Module for reading CSV files
import csv
#import csv file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #set variables and lists
    months = 0
    net = []
    date = []
    change = []
    #loop through the rows
    for row in csvreader:
        #The total number of months included in the dataset
        months+= 1 
        #create list of dates
        date.append(row[0])
        #The net total amount of "Profit/Losses" over the entire period
        net.append(int(row[1]))
        total = sum(net)
    #Loop through "net" to find the changes in "Profit/Losses" over the entire period, and then the average of those changes
    change = [net[row+1]-net[row] for row in range(len(net)-1)]
    avg_change = round((sum(change) / len(change)),2)
    #remove first date from date to align with change
    date.pop(0)
    # zip date and change
    list_zip = zip(date, change)
    zipped_change = list(list_zip)
    #The greatest increase in profits (date and amount) over the entire period (https://stackoverflow.com/questions/4800419/finding-max-value-in-the-second-column-of-a-nested-list)
    increase = max(zipped_change, key=lambda x: float(x[1]))
    #The greatest decrease in profits (date and amount) over the entire period
    decrease = min(zipped_change, key=lambda x: float(x[1]))
#create list of print output
lines = ["Financial Analysis",
"---------------------------------",
f"Total Months: {months}",
f"Total: ${total}",
f"Average Change: ${avg_change}",
f"Greatest Increase in Profits: {increase[0]} (${increase[1]})",
f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})"]
#Print output (https://stackoverflow.com/questions/13443588/how-can-i-format-a-list-to-print-each-element-on-a-separate-line-in-python)
print(*lines,sep='\n')

txtoutput = os.path.join('Analysis', 'financial_analysis.txt')
with open(txtoutput, 'w') as f:
    f.write('\n'.join(lines))