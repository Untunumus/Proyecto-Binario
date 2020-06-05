import time
import goslate
gs = goslate.Goslate()
import os
from tabulate import tabulate
def trans_late(language_id):
	"""
	La función traduce la base de datos(biblioteca) y la lista de mensages del programa.

	:param language_id: str. id de lenguaje de destino.
	:return: list. lista de mensajes traducida, lista de base de datos(biblioteca) traducida.
	"""
	global library
	global messages
	library = get_library()
	#messages = list(gs.translate(["not an a valid input please write a right one\n",#0
	messages = list(["not an a valid input please write a right one\n",#0
		'Do you want to enter a book (0) or do a search (1)?\n', #1
		'Insert a title for your book\n',#2
		'Insert an author for your book\n',#3
		'Insert an year for your book\n', #4
		'Insert a location for your book\n',#5
		'Insert a description for your book\n', #6
		'Title',#7
		'Author',#8
		'Year',#9
		'Location',#10
		'Description',#11
		'Insert keywords of the book you want\n',#12
		'Insert a description for your book\n',#13
		'Please select a searching category Title(0), Author(1), Year(2), Location(3), Description(4), Language(5), State(6)\n',#14
		'Insert keywords of the book you want\n',#15
		'The book is not found in the library\nThese are the books found in the library\n',#16
		'Thanks for using libraryriAutomata\n',#17
		'Do you wanna exit (1) or continue (0)?\n',#18
		'Results',#19
		'Language',#20
		'State',#21
		'Results in your language', #22
		'Insert a language id for your book\n',#23
		'Insert a state for your book\n'#23
		])#, language_id))
	#time.sleep(0.2)
	#for i in range(len(library)):
	#	library[i] = list(gs.translate(library[i], language_id))
	#	time.sleep(0.2)
	return messages, library

def language_menu(language_input):
	"""
	Pregunta por el  idioma del usuario. Llama a la función trans_late.

	:param language_input: int. Selección del usuario según la lista (inglés(0), español(1), francés(2), otro idioma(3)).
	:return: list. lista de mensajes traducida a la selección del usuario, lista de base de datos(biblioteca) traducida a la selección del usuario.
	"""
	while True:
		try:
			language_input = int(language_input)
			if language_input == 0:  
				messages, library = trans_late('en') 
				break
			elif language_input == 1:
				messages, library = trans_late('es')
				break
			elif language_input == 2:
				messages, library = trans_late('fr')
				break
			elif language_input == 3: 
				language_id = input('Please insert your language code\n')
				messages,library = trans_late(language_id)
				break
			else:
				os.system('cls')
				print("not an a valid input please write a right one")
				language_input = input("Select your language english(0),spanish(1), french(2) or a diferent language(3)\n")
				continue
		except: 
			os.system('cls')
			print("not an a valid input please write a right one")
			language_input = input("Select your language english(0),spanish(1), french(2) or a diferent language(3)\n")


	return messages, library


def add(title_input, author_input, year_input, location_input, description_input, language_input, state_input):
	"""
	Añade un libro a la base de datos(biblioteca). Llama a la función print_table

	:param title_input: str. Título del libro a añadir.
	:param author_input: str. Autor del libro a añadir.
	:param year_input: str. Año del libro a añadir.
	:param location_input: str. Locación del libro a añadir.
	:param description_input: str. descripción del libro a añadir.
	"""
	state_input += '\n'
	book = [title_input, author_input, year_input, location_input, description_input, language_input, state_input]
	library.append(book)
	library.sort()
	print(tabulate(library))
	save_library(library)

def search(category, book, language_input):
	"""
	Busca un libro preexistente en la biblioteca.

	:param category: int. Selección del usuario según la lista (Título(0), Autor(1), Año(2), Lugar(3), Descripción(4), Idioma(5), Estado(6)).
	:param book: str. Palabra clave de búsqueda.
	"""
	library.sort()
	boolean = False
	counter = 0
	language_counter = 0
	for i in range(len(library)):
		if book.lower() in library[i][category].lower():
			print('-'*90)
			print(messages[7]+": "+library[i][0].title())
			print(messages[8]+": "+library[i][1].title())
			print(messages[9]+": "+library[i][2].title())
			print(messages[10]+": "+library[i][3].title())
			print(messages[11]+": "+library[i][4].title())
			print(messages[20]+": "+library[i][5].title())
			print(messages[21]+": "+library[i][6].title())
			boolean = True
			counter += 1
			if library[i][5] == language_input :
				language_counter += 1
			continue
	else:
		if boolean:
			print('-'*90)
		else: 
			print(messages[16]) 
			print(tabulate(library))
	print(messages[19] + ': ' + str(counter))
	print(messages[20] + ': '+ str(language_counter))

def get_library():
	"""
	Obtiene la libreria del archivo library.txt
	:return: list. Lista de libros en la base de datos.
	"""

	library_file = open('library.csv', 'r')
	library = [line.split(',') for line in library_file if line != '\n']
	library_file.close()
	return library

def save_library(library):
	"""
	Guarda la librería en el archivo externo library.txt
	:param library: list. Lista de la biblioteca de libros
	"""
	library_file = open('library.csv', 'w')
	for book in library:
		if book != '\n':
			line = ','.join(book)
			library_file.write(line)
	library_file.close()