# Bryan Paynich
# 12/11/2018
# Python Challange - PyBank
# This assignment takes the contents of a csv file and completes some simple 
# financial analysis on the data. The python script extracts the total number 
# of months of data, Total values, Average change of balances month to month, 
# and differences in profits on a rolling monthly basis.

import os
import csv

#Arrays
list_month = []
list_value = []
difference_value = []

csvpath = os.path.join('', 'Resources', '03-Python_Homework_PyBank_Resources_budget_data.csv')

# Read CSV File 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        list_month.append(row[0])
        value = int(row[1])
        list_value.append(value)

    iterate_values = list(list_value) 
    lvalue = iterate_values.pop(0) 

    for x in iterate_values:
        diff = x - lvalue
        difference_value.append(diff)
        lvalue = x

    # Count number of entries
    count_list = len(list_value)
    
    # Total Value of all months
    total_value = sum(list_value)
    
    # Get Highest Increase in Profits Month
    max_value = max(difference_value) 
    for x in difference_value:
        if (str(x) == str(max_value)):
            max_month = int(difference_value.index(x)+1)
    high_month = list_month[int(max_month)]

    # Get Lowest Decrease in Profits Month 
    min_value = min(difference_value)
    for x in difference_value:
        if (str(x) == str(min_value)):
            min_month = int(difference_value.index(x)+1)
    low_month = list_month[int(min_month)]

    #Get average change month to month 
    diff_sum  = sum(difference_value)
    average_difference = str(round((diff_sum) / (count_list - 1),2))    

    # Print out report for all values
    print ("\n")
    print ("Financial Analysis")
    print ("--------------------------")   
    print ("Total Months: " + str(count_list))
    print ("Total: $" + str(total_value))
    print ("Average Change: $" + str(average_difference))
    print ("Greatest Increase in Profits: " + str(high_month) + " ($" + str(max_value) + ")")
    print ("Greatest Decrease in Profits: " + str(low_month)  + " ($" + str(min_value) + ")")

# save the output file path
output_file = os.path.join("pybank_output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------"])
    writer.writerow(["Total Months:", str(count_list)])
    writer.writerow(["Total:", "$" +  str(total_value)])
    writer.writerow(["Average Change:", "$" + str(average_difference)])
    writer.writerow(["Greatest Increase in Profits:", str(high_month), "($" + str(max_value) + ")"])
    writer.writerow(["Greatest Decrease in Profits:", str(low_month),  "($" + str(min_value) + ")"])