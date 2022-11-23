# coin_counter
takes weights of coins and returns if the user has collected the wrong amount of coins

        ANALYSIS
The program must:
• allow the user to input the volunteer’s name, type of coin and weight of bag
• validate the coin type
Inputting variables input boxes and buttons would be best
I also would have to add input validation try and except would be useful
• indicate the number of coins to be added or removed to correct an inaccurate
bag weight
If Accurate_bag_weight - current_bag_weight != 0:
• maintain running totals of the number of bags checked and total value
total_bags +=1, total_value += bag_cost
• provide an option to display the total number of bags checked and total value
• monitor the accuracy of the volunteers counting the coins
• provide an option to display a list of the volunteers, sorted by accuracy,
Showing:
o the total number of bags they have counted
o the number of bags they counted correctly, as a percentage of their total.
Gui menus using tkinter
• Save the data in a text file called CoinCount.txt
Database using a txt file using a list of dictionaries would be easy to read and code
• Load CoinCount.txt at the beginning of each session.
 File  = open(CoinCount.txt,a)
• Update CoinCount.txt at the end of each session.
Use  .append to save changes

I would like to add a gui using tkinter. This would make the program easier to use and view. I will use classes to help structure and group my code together, this will also come in handy whenever I open a different menu as I can use a different class instead of a new window.
I assume that the bags only contain one type of coin. This means i can find the accurate weight and subtract the bag's weight, this will tell me if the user is accurate. With accuracy I will use ratios of (correct_answers/wrong_answers) to determine the accuracy of the user. To store the information in a text file I will use a list of dictionaries that will be easy to read and import into the program.
            Evaluation

My program allows the user to input the volunteer’s name, type of coin and weight of bag using input boxes and dropdown menus that make the program easy to use no matter the user's experience. My program will validate the coin type because if the user is told to add a decimal amount of coins to the bag they will know the inputted the wrong value. The program will also indicate the number of coins to be added or removed to correct an inaccurate bag weight, I encountered an error with the 1p bags where it displayed an incorrect amount of coins to add this was due to a logic error where I wrote 3.65->3.56 this is now fixed.my program now maintains running totals of the number of bags checked and total value on a different menu that can be accessed and viewed using a dropdown menu bar.
On another window you can see the volunteers stats (accuracy as a percent and total bags checked) sorted by accuracy. This data is read out of a text file at the start of the program. It is then written into when the user save and quits.

