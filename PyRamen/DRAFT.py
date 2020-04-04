import os
import csv

#Data file locator
csvpath=os.path.join('Resources','menu_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    menu = []
    data = list(csvreader)

    for row in csvreader:

        item.append(row[0])
        category.append(row[1])
        description.append(row[2])
        price.append(row[3])
        cost.append(row[4])
        
print(menu)