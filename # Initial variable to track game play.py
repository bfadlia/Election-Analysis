# Initial variable to track game play
user_play = "y"
s = input("How many numbers you want to loop through: ")
# While we are still playing...

while user_play == "y":

    # Ask the user how many numbers to loop through

  

    for x in range(1,int(s)+1):
	    print(x)
    
    # Once complete...
user_play = input("Continue: (y)es or (n)o? ")
