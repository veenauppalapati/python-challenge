
# First we'll import the os module to create file paths across operating systems
import os

# import the csv module for reading CSV files
import csv

import statistics


def calc_avg(divident, divisor):
    average = (divident / divisor)
    return(round((divident / divisor),2))

# READING CSV FILE AND ANALYZING THE DATA

def main():


    # read csv files
    input_csv_file = os.path.join("Resources", "budget_data.csv")


    with open(input_csv_file) as text_file_stream:

        # CSV reader specifies delimiter and variable that holds contents
        csv_reader = csv.reader(text_file_stream, delimiter=',')

        
        # Read the header row first (skip this step if there is now header)
        csv_header = next(csv_reader)

        # calculate total number of dates
        total_dates = 0
        total_sum = 0
        budget_data_list=[]

        # Function 3 variables
        previousProfit_Losses = 0
        change_profit_losses_list = [] #will contain the difference between each month profit/loss
        total_change_profit_loss = 0
        greatest_increase_data = []
        average = 0.00
        mean_change = 0
        counter = 0


        #Read each each row of data after the header
        for row in csv_reader:

            #push the data from csv file to a list for later use
            budget_data_list.append([row[0],int(row[1])])

            # calcululate total number of dates
            total_dates = total_dates + 1
         
            # Retrieve the values from profits/losses
            profit_losses = int(row[1])

            # calculate net amount of profit/losses by accumulating the sum
            total_sum = total_sum + profit_losses

              
            
        # calculate mean change ( average change over an entire data set )
        for i in range(0, len(budget_data_list)-1):

            start_value = budget_data_list[i][1]
            end_value = budget_data_list[i+1][1]

            #Subtract the starting value from the ending value for each item in the data set. 
            mean_change = end_value - start_value

            #Append the mean change result to the specified array
            change_profit_losses_list.append(mean_change)

        
        #Calculate the average change
        average_change = calc_avg(sum(change_profit_losses_list),len(change_profit_losses_list))
    

        #Calculate greatest increase
        greatest_increase = max(change_profit_losses_list)
        greatest_increase_index = change_profit_losses_list.index(greatest_increase)
        greatest_increase_date = budget_data_list[greatest_increase_index][0]
       

         #Calculate greatest decrease
        greatest_decrease = min(change_profit_losses_list)
        greatest_decrease_index = change_profit_losses_list.index(greatest_decrease)
        greatest_decrease_date = budget_data_list[greatest_decrease_index][0]
        

        # Display the output
        print('#' * 100)
        print('\n')
        print('-'*35)
        print("Financial Analysis")
        print('-'*35)
        print (f"Total number of dates : {total_dates}")
        print(f"Total net amount: ${total_sum}")
        print(f"Average  Change: ${average_change}")
        print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
        print('\n')
        print('#' * 100)

main()

   
    




