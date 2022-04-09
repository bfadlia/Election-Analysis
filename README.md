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

## Summary
Analyzing the effect of using the refactored code:
- In general, using refactored code is very common in software development. The problem you are trying to solve must have been considered and tackled by many before you and if others work is available and well documented saves you a lot of time to start with their libraries and genric code and tailor it to your specific problem compared to writing everything you need from scratch. The only disadvantage is it takes some work and knowledge to know where to find trusted source of code to start with or misunderstanding deifferences between what they solved and what you are trying to solve.
- In the particular case of this original and refactored scripts, the original script had two nested loops repeating the looping through the entire records by the number of stocks thre are dedicating. The refactored script loops through the entire records only once so it's no surprise that the program ran more than 5 times faster with the refactored code. We can now be confident that this code will scale well when we have many more stocks.
