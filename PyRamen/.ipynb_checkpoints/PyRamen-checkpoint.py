# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources', 'menu_data.csv')
sales_filepath = Path('Resources', 'sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, newline='') as menufile:
    csvreader = csv.reader(menufile, delimiter=',')
    csv_header = next(csvreader)
    menu = []
    menu_data = list(csvreader)

    for row in csvreader:

        item = row[0]
        category = row[1]
        description = row[2]
        price = int(row[3])
        cost= int(row[4])
        
#print(menu_data)

# @TODO: Read in the sales data into the sales list

with open(sales_filepath, newline='') as salesfile:
    csvreadersales = csv.reader(salesfile, delimiter=',')
    csv_headersales = next(csvreadersales)
    sales = []
    sales_data = list(csvreadersales)

    for row in csvreadersales:

        Quantity = int(row[3])
        Menu_Item = row[4]
        
#print(sales_data[:10])
#print(sales_data) - IT CANT PRINT THAT MUCH!


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object ##SEE ABOVE##

    


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    
count = 0
revenue = 0
cogs = 0
profit = 0


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit


report = {
    "01-count": 0,
    "02-revenue": 0,
    "03-cogs": 0,
    "04-profit": 0,
}





    # @TODO: For every row in our sales data, loop over the menu records to determine a match



    
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
