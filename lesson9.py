'''Take two int values from user and print greatest among them.'''

# A = int(input('Tur 1-in tiv@ '))
# B = int(input('Tur 2-rd tiv@ '))
# if A > B:
# 	print(A)
# if B > A:
# 	print(B)
# if A == B:
# 	print("lol")	


'''Take input of age of 3 people by user and determine oldest and youngest among them.'''

# Arshak = int(input('Tur Arshak tariq@  '))
# Tiko = int(input('Tur Tiko tariq@  '))
# Aram = int(input('Tur Aram tariq@  '))
# if Arshak > Tiko and Arshak > Aram:
# 	print('Arshakna mec')
# if Arshak < Tiko and Arshak < Aram:
# 	print('Arshak@ poqra')
# if Tiko > Aram and Tiko > Arshak:
# 	print('Tikona mec')
# if Tiko < Aram and Tiko < Arshak:
# 	print('Tikona poqra')
# if Aram > Tiko and Aram > Arshak:
# 	print('Aramna mec ')
# if Aram < Arshak and Aram < Tiko:
# 	print('Aramna poqra')	
# if Arshak == Aram == Tiko:
# 	print("lol")	

'''You have number. Write a python program which to print a new number with digits reversed as of original one.''' 

# Tiv = int(input('Tur qaranish tiv '))
# A = Tiv % 10
# B = Tiv // 10 % 10 
# C = Tiv // 100 % 10 
# D = Tiv // 1000
# print(str(A) + str(B) + str(C) + str(D))

'''Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in
anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban
areas only.
And any other input of age should print "ERROR".'''
# Kargavichak = input('Amusnacac eq? Y/N =').upper()
# Tariq = int(input('Dzer tariq@ '))
# Ser = input('Dzer ser@ 1.A/2.I = ').upper() 
# if Ser != 2:
# 	print('Ancnenq araj') 
# elif Ser != 1:
# 	print('duq kashxateq miayn qaxaqum')
# if Tariq >= 20 and Tariq <= 40 : 
# 	print('Duq karox eq ashxatel vortex uzum eq')
# elif Tariq > 40 and Tariq <= 60:
# 	print('Dzer hamar ashxatanq ka miayn qaxaqum') 
# else:
# 	print('ERROR')


'''Rock, Paper, Scissors'''

# import random

# user_action = input("Enter a choice (rock, paper, scissors): ")
# possible_actions = ["rock", "paper", "scissors"]
# computer_action = random.choice(possible_actions)
# print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
# balans = 0
# balans1 = 0
# if user_action == computer_action:
#     print(f"Both players selected {user_action}. It's a tie!")
# elif user_action == "rock":
#     if computer_action == "scissors":
#         print("Rock smashes scissors! You win!")
#         balans += 500
#         balans1 -= 500
#         print(balans1, 'PC',balans, 'User')
#     else:
#         print("Paper covers rock! You lose.")
#         balans -= 500
#         balans1 += 500
#         print(balans1,'PC',balans,'User') 
# elif user_action == "paper":
#     if computer_action == "rock":
#         print("Paper covers rock! You win!")
#         balans += 500
#         balans1 -= 500
#         print(balans1,'PC',balans,'User')
#         print("Scissors cuts paper! You lose.")
#         balans -= 500
#         balans1 += 500
#         print(balans1,'PC',balans,'User')
# elif user_action == "scissors":
#     if computer_action == "paper":
#         print("Scissors cuts paper! You win!")
#         balans += 500
#         balans1 -= 500
#         print(balans1,'PC',balans,'User')
#     else:
#         print("Rock smashes scissors! You lose.")
#         balans -= 500
#         balans1 += 500
#         print(balans1,'PC',balans,'User')

'''You (input) and pc have followers (pc have random followers) if your followers is great 20 % than pc you are blogger otherwise pc is blogger.'''
# from random import randint as r 

# Arshak = int(input('Tur inc qo folovneri qanak@ '))
# pc = r(100,1000)
# if pc + pc * 0.2 < Arshak:
# 	print('Arshak@ haxtec')
# else:
# 	print('pc haxtec')

'''You and the Pc take part in the rally, You must pass 12 km. PC passed in 3 minutes and You are 10% later than Pc. how much is the speed of your car.'''

# S = 12
# T = 180
# A = (T * 10 / 100 + 180) / 60
# print(A)
# K = 12 / A
# print(K)