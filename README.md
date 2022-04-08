# Election Audit Project

## Overview of Project


 - This project helps is intended to help election officials obtain the election results from a csv file that contains the raw voting data. After an initial effort the officials requested the following additions:
 - The election commission has requested some additional data to complete the audit:
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
- The project will deliver these and votes counts and percentages of each candidate as well as pointing out the winner who got the highest votes


## Results

The original code is in module 1 and the refasctored is in module 2 in the VBA script

The results of the refactored project were as follows:
- For 2017:
  - ![IMAGE_DESCRIPTION](/resources/VBA_Challenge_2017.png)
- For 2018
  - ![IMAGE_DESCRIPTION](/resources/VBA_Challenge_2018.png)
- The refactored code runs more than five times faster than the original code
- Most stocks analyzed did well in 2017 and most did poorly in 2018
## Summary
Analyzing the effect of using the refactored code:
- In general, using refactored code is very common in software development. The problem you are trying to solve must have been considered and tackled by many before you and if others work is available and well documented saves you a lot of time to start with their libraries and genric code and tailor it to your specific problem compared to writing everything you need from scratch. The only disadvantage is it takes some work and knowledge to know where to find trusted source of code to start with or misunderstanding deifferences between what they solved and what you are trying to solve.
- In the particular case of this original and refactored scripts, the original script had two nested loops repeating the looping through the entire records by the number of stocks thre are dedicating. The refactored script loops through the entire records only once so it's no surprise that the program ran more than 5 times faster with the refactored code. We can now be confident that this code will scale well when we have many more stocks.
