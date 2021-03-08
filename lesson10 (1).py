'''Write a Python program to check if pc number is great than 10. random(1,20) when True break.'''

# import random

# while True:
# 		A = random.randint(1,20)
# 		print(A)
# 		if A > 10 :
# 			break


'''Chinga Chung'''
# import random


# possible_actions = ["rock", "paper", "scissors"]
# computer_score = 0
# player_score = 0
# while player_score < 3 and computer_score < 3:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#             player_score += 1
#             print(computer_score, 'PC',player_score, 'User')
#         else:
#             print("Paper covers rock! You lose.")
#             computer_score += 1
#             print(computer_score,'PC',player_score,'User') 
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#             player_score += 1
#             print(computer_score,'PC',player_score,'User')
#         else:
#             print("Scissors cuts paper! You lose.")
#             computer_score += 1
#             print(computer_score,'PC',player_score,'User')
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#             player_score += 1
#             print(computer_score,'PC',player_score,'User')
#         else:
#             print("Rock smashes scissors! You lose.")
#             computer_score += 1
#             print(computer_score,'PC',player_score,'User')
