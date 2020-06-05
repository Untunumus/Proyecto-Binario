import main as mn
def create_account(dicctionary):
	try:
		create_acount = int(input('Do you want to create a new account? Yes(0), No(1)\n'))
		while create_acount not in range(2):
			print('wrong input insert anotherone')
			create_acount = int(input('Do you want to create a new account? Yes(0), No(1)\n'))
		if create_acount == 0:
			new_username = input('Write the new username')
			while new_username not in dicctionary:
				if new_username == input('Confirm your username'):
					new_password = input('Write your password')
					while True:
						if new_password == input('Confirm your password'):
							dicctionary[new_username] = new_password
							with open('users.dat', '+a') as users:
								users.Write('\n{}:{}'.format(new_username, new_password))
							break
						else:
							print('Your passwords are different')
					break
				else:
					print('Your usernames are different')
			else:
				print("The user you're trying to register is allready in the system" )
				signin()
		else:
			reading_version = input('Do you want to enter to an only reding version? Yes(0), No(1)')
			
	except:
		print('error')


def get_users():
	users = open('users.dat', 'r')
	user_dic = {}
	for line in users:
		if line != '\n':
			user = tuple(line.split(':'))
			user_dic[user[0]] = user[1]
	return user_dic

def confirm_user(dicctionary, user_input):
	
	if user_input in dicctionary.keys() and user_input != '':
		password_input = input()
		iterador = 0
		while iterador <= 5:
			if dicctionary[user_input] == password_input:
				print('hello')
				mn.main()
				break
			else: 
				print('wrong password')
				password_input = input()
				iterador += 1
		else:
			print('You have exced the number of antemps allowed')
	else:
		create_account(dicctionary)
		

def signnin():
	user_input  = input()
	user_dic = get_users()
	confirm_user(user_dic, user_input)

signin()
