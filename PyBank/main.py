import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(os.path.abspath(budget_data)) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    pl = [] 
    dates = []
    skip_head = 1

    for row in csvreader:

        if skip_head:
            skip_head = 0
        else:
            pl.append(int(row[1]))
            dates.append(row[0])

    row_count = len(pl)

    sum = 0
    prev_row = 0
    total_change = 0
    skip_head = 1

    changes = []

    for row in pl:
        sum += row
        if skip_head:
            skip_head = 0
        else: 
            total_change += row - prev_row
            changes.append(row-prev_row)
        prev_row = row

    max_increase = 0
    max_increase_index = 0
    max_decrease = 0
    max_decrease_index = 0
    index = 0

    for row in changes:
         if row > max_increase:
            max_increase = row
            max_increase_index = index+1

         if row < max_decrease:
            max_decrease = row
            max_decrease_index = index+1
        
         index += 1

    increase_parts = dates[max_increase_index].split("-")
    decrease_parts = dates[max_decrease_index].split("-")

    print(row_count)
    print(f'${sum}')
    print(f'${total_change/(row_count-1):.2f}')
    print(f'Greatest Increase in Profits:{increase_parts[1]}-{increase_parts[0]} $({max_increase})')
    print(f'Greatest Decrease in Profits:{decrease_parts[1]}-{decrease_parts[0]} $({max_decrease})')
    