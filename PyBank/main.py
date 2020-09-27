
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

        print(csv_reader)

        # Read the header row first (skip this step if there is now header)
        csv_header = next(csv_reader)
        print(f"CSV Header: {csv_header}")

        lines = text_file_stream.read()
        print(lines)


main()

   
    




