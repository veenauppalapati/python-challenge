import os
import csv

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

          

def main():

    election_data_list = []
    read_input_file(election_data_list)

    print(election_data_list[0])

main()