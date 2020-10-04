
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

def calculate_candidates_votes(input_list):

    candidate_one_count = 0
    candidate_two_count = 0
    candidate_three_count = 0
    candidate_four_count = 0
    
    for row in input_list:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        

        if candidate == "Correy":
            candidate_one_count = candidate_one_count + 1
        elif candidate == "Khan":
            candidate_two_count = candidate_two_count + 1
        elif candidate == "Li":
            candidate_three_count = candidate_three_count + 1
        elif candidate == "O'Tooley":
            candidate_four_count = candidate_four_count + 1


    # create a dictionary
    candidate_votes_dict = {"Correy": [candidate_one_count],
                        "Khan": [candidate_two_count], 
                        "Li": [candidate_three_count],
                        "O'Tooley": [candidate_four_count]}         
    


    return candidate_votes_dict
        

# --------------------------------------------------------------------------------

def calculate_votes_percentage(input_dict, total):


    #For each key in the dictionary 
    for key, val in input_dict.items():
        
        # Calculate and round the percentage
        percentage = round(((val[0] / total) * 100), 2)
        
        #push the percentage value to the candidate's value list
        val.append(percentage)

        # Set the percentage value for each candidate
        input_dict[key] = val

    return input_dict

# --------------------------------------------------------------------------------

def determine_winner(input_dict):

    votes_list = []

    # List out the keys separately
    candidates_list = list(input_dict.keys()) 
    print(candidates_list)

    # List out the values separately
    items = input_dict.values()

    for item in items:
        votes_list.append(item[0])

    # Determine the max value
    winner_votes = max(votes_list)
    print(winner_votes)

    # Retrieve the key of the max value
    winner = candidates_list[votes_list.index(winner_votes)]
    
    
    return winner

 # --------------------------------------------------------------------------------   

def print_output(input_dict, input_winner, input_total_votes):
    formatted_title = ''
    print('#' * 100 + '\n')
    title = "Election Results"
    for letter in title:
        formatted_title = formatted_title + (letter + ' ')
    print (formatted_title.upper())
    print('-'*35)
    print(f"Total Votes: {input_total_votes}")
    print('-'*35)
    for key, val in input_dict.items():
        votes = val[0]
        vote_percentage = val[1]
        print(f"{key}: {vote_percentage}% ({votes})") 
    print('-'*35) 
    print(f"Winner: {input_winner}")
    print('-'*35)
    print('\n'+'#' * 100 )

 # --------------------------------------------------------------------------------   

# Define the main function       

def main():

    election_data_list = []
    total_votes = 0
     
    
    # Call read_input_file function: Read the election_data.csv file and push the data into a list
    read_input_file(election_data_list)
 
    #calculate the total number of votes cast
    total_votes = len(election_data_list)


    # Calculate total votes for each candidate
    votes_dict = calculate_candidates_votes(election_data_list)
   

    # Calculate the percentage of votes each candidate won
    candidate_dict = calculate_votes_percentage(votes_dict, total_votes)
   

    # The winner of the election based on popular vote
    winner = determine_winner(candidate_dict)

    # Display the output
    print_output(candidate_dict, winner, total_votes)

# --------------------------------------------------------------------------------
main()