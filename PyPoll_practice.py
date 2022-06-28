# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))
#file_to_load = 'election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

# Print the file object
     print(election_data)
# Close the file
#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Use the open statement to open the file as a text file
#outfile = open(file_to_save,"w")
# Write some data to the file
#outfile.write("Hello World")

# Using the with statement to open the file as a txt file
with open(file_to_save,"w") as txt_file :

# write some data to the file
   txt_file.write("Hello World using WITH function")     

# Write three counties to the file
   txt_file.write("Arapahoe, Denver, Jefferson")
     
# Write three counties to the file with next line.
   txt_file.write("\n\nCounties in election")     
   txt_file.write("\n--------------------")
   txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()