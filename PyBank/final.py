#Import Modules
import os
import csv 

#Data file locator
csvpath=os.path.join('Resources','budget_data.csv')

#set the output of the text file
text_path = "results.txt"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []        

#Months as per Date column       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
   
 ##GOOD! print(len(month))
    
#Revenue as per Profit/Losses column
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    
##GOOD!    print(total_revenue)

#Average Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 
 #Append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    
    monthly_change = Total / len(revenue_change)

##GOOD!    print(round(monthly_change, 2))
    
    
#Greatest Revenue Increase
    profit_increase = max(revenue_change)

##GOOD!    print(profit_increase)
    
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Revenue Decrease
    profit_decrease = min(revenue_change)

##GOOD!    print(profit_decrease)
    
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis')
print(f'----------------------------')
print("Total Months: " + str(len(month)))
print("Total: $" + str(total_revenue))      
print("Average Change: $" + str(round(monthly_change,2)))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

#write changes to csv
with open(text_path, 'w') as file:
    file.write(f'Financial Analysis\n')
    file.write(f'----------------------------\n')
    file.write("Total Months: " + str(len(month)))
    file.write("\n")
    file.write("Total: $" + str(total_revenue))
    file.write("\n")
    file.write("Average Change: $" + str(round(monthly_change,2)))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

    
