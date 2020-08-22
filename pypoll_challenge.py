import os
import csv
filepath = os.path.join("election_results.csv")
filepath

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(filepath, mode="r") as fread:
  csv_reader = csv.reader(fread)
  header = next (csv_reader)
 

  for row in csv_reader:
   # 2. Add to the total vote count.
      total_votes += 1
        # Get the candidate name from each row.
      candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
      if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1

election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"                        \n")
print(election_results)

county_options = []
county_votes = {}     
largest_county = ""
largest_count = 0
winning_percentage = 0

with open(filepath, mode="r") as fread:
  csv_reader = csv.reader(fread)
  header = next (csv_reader)

  for row in csv_reader:
   # 2. Add to the total vote count.
      total_votes += 1
        # Get the county name from each row.
      county_name = row[1]
        # If the county does not match any existing county add it the
        # the county list.
      if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
      county_votes[county_name] += 1

for county_name in county_votes:
    # Retrieve vote count and percentage.
    votes = county_votes[county_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.

    print(f"County Votes:\n"
        f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine largest vote count, winning percentage, and county.
    if (votes > largest_count) and (vote_percentage > winning_percentage):
        largest_count = votes
        largest_county = county_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
County_Vote_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    f"-------------------------\n")

print(County_Vote_summary)

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(filepath, mode="r") as fread:
  csv_reader = csv.reader(fread)
  header = next (csv_reader)

  for row in csv_reader:
   # 2. Add to the total vote count.
        # Add to the total vote count.
      total_votes += 1
        # Get the candidate name from each row.
      candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
      if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1


for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    print(f"Candidate Votes:\n"
    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

with open("Election_Results.txt", "w") as txt_file:
  txt_file.write(election_results)
  
  for county_name in county_votes:
    # Retrieve vote count and percentage.
    votes = county_votes[county_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.

    txt_file.write(f"County Votes:\n"
        f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
  
  txt_file.write(County_Vote_summary)
  
  for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    
    txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  
  txt_file.write(winning_candidate_summary)

  
 
