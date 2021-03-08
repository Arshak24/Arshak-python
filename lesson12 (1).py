import random

ch = random.choice('pu')
balans_user = 0
balans_pc = 0
point = 0
if ch == 'u':
	print('User Start')
	while True:


		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break


 	

		pc = 4 - point % 4
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break
	

else:
	print('Start pc')
	while True:
		if point % 4 == 0:
			pc = random.randint(1,3)
		else:	

			pc = random.randint(1,3)
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break



		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break

ch = random.choice('pu')

point = 0
if ch == 'u':
	print('User Start')
	while True:


		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break


 	

		pc = 4 - point % 4
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break
	

else:
	print('Start pc')
	while True:
		if point % 4 == 0:
			pc = random.randint(1,3)
		else:	

			pc = random.randint(1,3)
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break



		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break

ch = random.choice('pu')

point = 0
if ch == 'u':
	print('User Start')
	while True:


		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break


 	

		pc = 4 - point % 4
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break
	

else:
	print('Start pc')
	while True:
		if point % 4 == 0:
			pc = random.randint(1,3)
		else:	

			pc = random.randint(1,3)
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			balans_user += 1
			print('pc',balans_pc,'user',balans_user)
			break



		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break

				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			balans_pc += 1
			print('pc',balans_pc,'user',balans_user)
			break
			if balans_user == 3:
				print('GG')
			else:
				print('Game over')		