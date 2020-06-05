def leer_archivo():
  try:
    with open('archivos/Bogota_covid19.csv', 'r', encoding='LATIN-1') as archivo:
      datos = {}
      datos_lista = [linea.split(',') for linea in archivo]
      for i in range(len(datos_lista[0])):
        vertical =[linea[i] for linea in datos_lista]
        datos[vertical[0]] = vertical[1:]
    return datos
  except:
    print('El archivo Bogota_covid19.csv no existe en el diccionario "archivos"')
    

def menu_principal():
  seleccion = input("""Bienvenido a Bogota Covid-19 Statistical Program, recuerde, lavese las manos cada tres horas y quedese en casa.
  \nEste es el menu principal, escriba el numero que este al frente de la opcion que desea elegir y presione la tecla enter.
  \n\t 1) Leer datos.
  \n\t 2) Ver estadisticas por localidad.
  \n\t 3) Ver la cantidad de contagiados en un rango de tiempo.
  \n\t 4) Ver las tres localidades con mayor numero de contagios.
  \n\t 5) Descargar las estadisticas por tipo de caso.
  \n\t 6) Descargar las estadisticas generales.
  \n\t 7) Salir\n""")
  if seleccion == 1:
    
  
def estadisticas_localidad(localidad, datos):
  
  while True:
    selecccion = input("""Bienvenido al menu de estadisticas por localidad, seleccione 
  \n\t 1) Ver el total de contagiados.
  \n\t 2) Ver la cantidad de contagiados por genero.
  \n\t 3) Ver la cantidad de contagiados por tipo de caso.
  \n\t 4) Ver la cantidad de contagiados por ubicación.
  \n\t 5) Ver la cantidad de contagiados por rango de edad.
  \n\t 6) Ver la cantidad de contagiados por estado.
  \n\t 7) Salir.\n""").lower()
    if seleccion =='7':
      menu_principal()
      break
    elif seleccion ==	 '1': 
      contador = 0
      for i in datos['Localidad de residencia']:
        if i == localidad.lower():
          contador += 1
      print('Total de contagiados:', contador)
      break
    elif seleccion == '2':
      hombres = 0
      mujeres = 0
      for i in range(len(datos['Localidad de residencia'])):
        if datos['Localidad de residencia'][i] == localidad.lower():
          if datos['Sexo'][i] = 'M':
            hombres += 1
          else:
            mujeres += 1 
      print('Hombres:', hombres)
      print('Mujeres:', mujeres)
      break
    elif seleccion == '3':
      en_estudio = 0
      importado = 0
      relacionado = 0 
      for i in range(len(datos['Localidad de residencia'])):
        if datos['Localidad de residencia'][i] == localidad.lower():
          if datos['Tipo de caso'][i] = 'En estudio':
            en_estudio += 1
          elif datos['Tipo de caso'][i] = 'Importado':
            importado += 1
          elif datos['Tipo de caso'][i] = 'Relacionado':
            relacionado = 0
      print('En estudio:', en_estudio)
      print('Importado:', importado)
      print('Relacionado', relacionado)
      break
    elif seleccion == '4':
      casa = 0
      hospital = 0
      fallecido = 0
      for i in range(len(datos['Localidad de residencia'])):
        if datos['Localidad de residencia'][i] == localidad.lower():
          if datos['Ubicación'][i] = 'Casa':
            casa += 1
          elif datos['Ubicación'][i] = 'Holspital':
            hospital += 1
          elif datos['Ubicación'][i] = 'Fallecido':
            fallecido += 1
      print('Casa:', casa)
      print('Hospital', hospital)
      print('Fallecido', fallecido)
      break
    elif seleccion == '5':
      _0_15 = 0
      _16_30 = 0
      _31_45 = 0
      _46_60 = 0
      _61_75 = 0
      _76_90 = 0
      _91+ = 0
      for i in range(len(datos['Localidad de residencia'])):
        if datos['Localidad de residencia'][i] == localidad.lower():
          if int(datos['Edad'][i]) >= 0 and int(datos['Edad'][i]) < 15:
            _0_15 += 1
          elif int(datos['Edad'][i]) >= 16 and int(datos['Edad'][i]) < 30:
            _16_30 += 1
          elif int(datos['Edad'][i]) >= 31 and int(datos['Edad'][i]) < 45:
            _31_45 += 1
          elif int(datos['Edad'][i]) >= 46 and int(datos['Edad'][i]) < 60:
            _46_60 += 1
            
            
            
           
	if seleccion != '7':        
		estadisticas_localidad()
        
      
      	
      
        
    
    
    
    
    