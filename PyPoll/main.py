
# Import required modules
import os
import csv

# Define read_input_file function:  Read the election_data.csv file and push the data into a list
def read_input_file(input_list):

    # define the path for the input file
    input_csv_file = os.path.join("Resources", "election_data.csv")

    with open(input_csv_file) as text_file_stream:

        # CSV reader specifies delimiter and variable that holds contents
        csv_reader = csv.reader(text_file_stream, delimiter=',')

        # Read the header row first (skip this step if there is now header)
        csv_header = next(csv_reader)
    

        #Read each each row of data after the header
        for row in csv_reader:

            input_list.append([int(row[0]), row[1], row[2]])

# --------------------------------------------------------------------------------

# Define the main function       

def main():

    election_data_list = []
    total_votes = 0
    
    # Call read_input_file function: Read the election_data.csv file and push the data into a list
    read_input_file(election_data_list)
 
    #calculate the total number of votes cast
    total_votes = len(election_data_list)


    # Display the output
    print(f"Total Votes: {total_votes}")

# --------------------------------------------------------------------------------
main()