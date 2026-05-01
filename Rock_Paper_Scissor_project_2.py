"""
WORKFLOW OF PROJECT : 
1. Input from user(Rock,Paper,Scissor)
2. Computer choice(computer will choose randomaly not Conditionally)
3. input print

Cases : 
A - Rock

Rock - Rock = tie
Rock - Paper = Paper
Rock - scissor = Rock

B - Paper 

Paper - Paper = tie
Paper - Rock = paper
Paper - scissor = Scissor

C - Scissor

Scissor - Scissor = tie
Scissor - Rock = Rock
Scissor - Paper = Scissor
"""
import random
item_list = ["Rock" , "Paper", "Scissor"]

user_choice = input("Enter your move :Rock,Paper,Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice} , computer choice = {comp_choice}")

if user_choice == comp_choice: 
    print("Both chooses same = Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper cover Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("paper cover Rock = You Win")
    else:
        print("Scissor cuts paper = Computer Win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor = Computer Win")
    else:
        print("Scissor cuts Paper = You Win")
