import os
import csv

#bring in file
budget_data = os.path.join("Resources", "budget_data.csv")

#save output as list
output = []

#read the csv file
with open(os.path.abspath(budget_data)) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #saves csv data to lists, create skip header row variable
    pl = [] 
    dates = []
    skip_head = 1

    #loop through data and save to lists
    for row in csvreader:

        if skip_head:
            skip_head = 0
        else:
            pl.append(int(row[1]))
            dates.append(row[0])

    #count rows
    row_count = len(pl)

    #creating counters
    sum = 0
    prev_row = 0
    total_change = 0
    skip_head = 1

    #list to hold changes
    changes = []

    #calculates change between rows
    for row in pl:
        sum += row
        if skip_head:
            skip_head = 0
        else: 
            total_change += row - prev_row
            changes.append(row-prev_row)
        prev_row = row

    #create tracking variables for max increase and decrease
    max_increase = 0
    max_increase_index = 0
    max_decrease = 0
    max_decrease_index = 0
    index = 0

    #find max increase and decrease in the changes list 
    for row in changes:
         if row > max_increase:
            max_increase = row
            max_increase_index = index+1

         if row < max_decrease:
            max_decrease = row
            max_decrease_index = index+1
        
         index += 1

    #formats the date below
    increase_parts = dates[max_increase_index].split("-")
    decrease_parts = dates[max_decrease_index].split("-")

    #print statements
    output.append(row_count)
    output.append(f'${sum}')
    output.append(f'${total_change/(row_count-1):.2f}')
    output.append(f'Greatest Increase in Profits:{increase_parts[1]}-{increase_parts[0]} $({max_increase})')
    output.append(f'Greatest Decrease in Profits:{decrease_parts[1]}-{decrease_parts[0]} $({max_decrease})')
    
    #output to a text file
    with open ("output.txt","w") as f:
        f.writelines(output)
    #output to terminal
    for line in output: 
        print(line)