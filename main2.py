#Isntalar lirería goslate desde el pip
#Favor utilizar el programa un número reducido de veces para evitar el banneo(de google) de la ip. 
import time
import goslate
gs = goslate.Goslate()
import functions2 as fn
import os
from tabulate import tabulate
def main():
	Exit = 0	
	language = input("Please select your language english(0),spanish(1), french(2) or a diferent language(3)\n")
	messages, library = fn.language_menu(language)
	while Exit != 1:
		while True:
			try:
				search_or_add_input = int(input(messages[1]))
				if search_or_add_input == 0:
					os.system('cls')
					title = input(messages[2]+'')
					author = input(messages[3]+'')
					year = input(messages[4]+'')
					location = input(messages[5]+'')
					descritpion = input(messages[6]+'')
					language_input = input(messages[23]+'')
					state = input(messages[24]+'')
					fn.add(title, author, year, location, descritpion, language_input, state)
				elif search_or_add_input == 1: 
					os.system('cls')	
					while True:
						category = input(messages[14])
						try:
							category = int(category)
							if category not in range(7):
								print(messages[0])
								continue
							break
						except:
							os.system('cls')
							print(messages[0])
							continue
					book = input(messages[15])
					fn.search(category, book, language)
				else:
					os.system('cls')
					print(messages[0])
					continue
				break
			except: 
				os.system('cls')
				print(messages[0])
		while True:
			Exit = input(messages[18])
			try:
				Exit = int(Exit)
				if Exit not in range(2):
					print(messages[0])
					continue
				break
			except:
				os.system('cls')
				print(messages[0])
			
	os.system('cls')
	print('\n'+messages[17])
	time.sleep(8)

#gs.translate(string, codigo idioma) traducir
#gs.detect(string) detectar idioma 
#fn.nombre_de_función 
#archivo.seek(índice) lleva al cursor al índice