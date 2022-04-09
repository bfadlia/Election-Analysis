# Election Audit Project

## Overview of the Project


This project is intended to help election officials obtain the election results from a csv file that contains the raw voting data. After an initial effort the officials requested the following additions:
  - The election commission has requested some additional data to complete the audit:
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
The project will deliver these and votes counts and percentages of each candidate as well as pointing out the winner who got the highest votes. The results will be printed to the terminal and also saved to a file.


## Results

- The results of the elections as calculated by our project were as follows:
    - Total Votes: 369,711
    - County Votes:
      - Jefferson: 10.5% (38,855)
      - Denver: 82.8% (306,055)
      - Arapahoe: 6.7% (24,801)
    - Largest County Turnout: Denver
    - Votes per candidate:
      - Charles Casper Stockham: 23.0% (85,213)
      - Diana DeGette: 73.8% (272,892)
      - Raymon Anthony Doane: 3.1% (11,606)
    - Election Winner: Diana DeGette
      - His Winning Vote Count: 272,892
      - His Winning Percentage: 73.8% 
  
- This information as saved in the output file:

  - ![IMAGE_DESCRIPTION](/Resources/results-file.png)
- Same output was optained live on the computer terminal running the script
  - ![IMAGE_DESCRIPTION](/Resources/results-terminal.png)

## Election Audit Summary and Suggestions for future use

With the script successfully and efficiently tallying and summarizing the election results, we suggest to the election commission its use can be expanded as follows:
  - A column is added to the csv file that indicates the type of election each vote row is for (presidential, congressional, house, governor. The program will contain additional conditions while looping to examine each record to figure out the type of election that vote pertains to and tallies it to its correct bucket.
  - The program would output at once all the voting results grouped by their election type saving a lot of resources and time.

