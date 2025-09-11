# Rock Paper Scissor Game
choices = ["rock", "paper", "scissor","rock", "paper", "scissor","rock", "paper", "scissor"]

# Rules

# 1, rock - paper -> paper win
# 2, rock - scissor -> rock win
# 3, paper - scissor -> scissor win


# Tasks

# Player inputs a choice
# System randomly select one
# If both select same option, then its a tie
# If its different then find find winner by the above rules


import random
user_answer = input("rock, paper, or scissor : ")
bot_answer = random.choice(choices)
print("bot answer : " ,bot_answer)


if bot_answer == user_answer:
    print("it's a tie")
elif (bot_answer == "rock" and user_answer == "scissor") or (bot_answer == "paper" and user_answer == "rock") or (bot_answer == "scissor" and user_answer == "paper") :
    print("Bot Wins!")
else:
    print("User Wins!")
    