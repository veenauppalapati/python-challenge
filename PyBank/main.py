
def calc_avg(divident, divisor):
    average = (divident / divisor)
    print(f"average : {average}")

# READING CSV FILE AND ANALYZING THE DATA

def main():

    # First we'll import the os module to create file paths across operating systems
    import os

    # import the csv module for reading CSV files
    import csv

    # read csv files
    input_csv_file = os.path.join("Resources", "budget_data.csv")


    with open(input_csv_file) as text_file_stream:

        # CSV reader specifies delimiter and variable that holds contents
        csv_reader = csv.reader(text_file_stream, delimiter=',')

        
        # Read the header row first (skip this step if there is now header)
        csv_header = next(csv_reader)
        print(f"CSV Header: {csv_header}")

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

            #Function 3 steps
            
            #subtract previousProfit_Losses from the current value in column 2
            if total_dates == 1:
                change_profit_losses_list.append(int(row[1]))
            else:
                #change_profit_losses_list.append(previousProfit_Losses - int(row[1]))
                change_profit_losses_list.append(int(row[1]) - previousProfit_Losses)
            previousProfit_Losses = profit_losses
            

        
        average = (sum(change_profit_losses_list) / len(change_profit_losses_list))

        print(round(average, 2))
        greatest_increase = max(change_profit_losses_list)
        greatest_increase_index = change_profit_losses_list.index(greatest_increase)
        greatest_increase_date = budget_data_list[greatest_increase_index][0]
        print(greatest_increase_date)

        print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        print(min(change_profit_losses_list))


                
    
        
        # Display the output
        print (f"Total number of dates : {total_dates}")
        print(f"Total net amount: {total_sum}")
  
        


main()

   
    




