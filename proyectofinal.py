# -*- coding: utf-8 -*-

# Importamos csv
import csv

# Inicializamos el código en el que igualamos una variable al comienzo, donde escribimos el nombre del archivo
# y la letra correspondiente para lo que lo vamos a utilizar(en este caso 'w' que es de escritura). 'w' detecta si el archivo
# no esta creado, y lo crea.
f = open('tiempo.csv', 'w')

# Creamos un array en el que le pasamos los campos principales de la tabla
campos = ['Estacion Meteorologica', 'Provincia', 'Temperatura Max', 'Hora(Temp Max)', 'Temperatura Min', 'Hora(Temp Min)']

# Igualamos la variable writer a DictWriter que rea un objeto que funciona como un lector normal, pero asigna la información de cada fila a un OrderedDict.
writer = csv.DictWriter(f, fieldnames=campos, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)

# A continuación introducimos datos
writer.writeheader()
writer.writerow({'Estacion Meteorologica': 'Estaca de Bares', 'Provincia': 'A Coruña', 'Temperatura Max': '18.3',
                     'Hora(Temp Max)': '12:50', 'Temperatura Min': '15.9', 'Hora(Temp Min)': '12:50'})
writer.writerow({'Estacion Meteorologica': 'As Pontes', 'Provincia': 'A Coruña', 'Temperatura Max': '22.4',
                     'Hora(Temp Max)': '15:30', 'Temperatura Min': '8.3', 'Hora(Temp Min)': '15:30'})
writer.writerow({'Estacion Meteorologica': 'A Coruña', 'Provincia': 'A Coruña', 'Temperatura Max': '19.7',
                     'Hora(Temp Max)': '13:40', 'Temperatura Min': '14.0', 'Hora(Temp Min)': '13:40'})
writer.writerow({'Estacion Meteorologica': 'A Coruña Aeropuerto', 'Provincia': 'A Coruña', 'Temperatura Max': '21.7',
                     'Hora(Temp Max)': '16:00', 'Temperatura Min': '8.5', 'Hora(Temp Min)': '16:00'})
writer.writerow({'Estacion Meteorologica': 'Villarrobledo', 'Provincia': 'Albacete', 'Temperatura Max': '23.4',
                     'Hora(Temp Max)': '16:40', 'Temperatura Min': '6.9', 'Hora(Temp Min)': '16:40'})
writer.writerow({'Estacion Meteorologica': 'Munera', 'Provincia': 'Albacete', 'Temperatura Max': '21.8',
                     'Hora(Temp Max)': '15:50', 'Temperatura Min': '2.2', 'Hora(Temp Min)': '15:50'})
writer.writerow({'Estacion Meteorologica': 'Yeste Embalse Fuensanta', 'Provincia': 'Albacete', 'Temperatura Max': '25.0',
                     'Hora(Temp Max)': '16:30', 'Temperatura Min': '7.2', 'Hora(Temp Min)': '16:30'})
writer.writerow({'Estacion Meteorologica': 'Nerpio', 'Provincia': 'Albacete', 'Temperatura Max': '20.6',
                     'Hora(Temp Max)': '15:40', 'Temperatura Min': '3.5', 'Hora(Temp Min)': '15:40'})
writer.writerow({'Estacion Meteorologica': 'Vélez Blanco - Topares', 'Provincia': 'Almería', 'Temperatura Max': '20.4',
                     'Hora(Temp Max)': '16:20', 'Temperatura Min': '9.8', 'Hora(Temp Min)': '16:20'})
writer.writerow({'Estacion Meteorologica': 'Adra', 'Provincia': 'Almería', 'Temperatura Max': '24.1',
                     'Hora(Temp Max)': '15:40', 'Temperatura Min': '15.7', 'Hora(Temp Min)': '15:40'})
writer.writerow({'Estacion Meteorologica': 'El Ejido', 'Provincia': 'Almería', 'Temperatura Max': '25.4',
                     'Hora(Temp Max)': '14:50', 'Temperatura Min': '14.2', 'Hora(Temp Min)': '14:50'})
writer.writerow({'Estacion Meteorologica': 'Roquetas de Mar', 'Provincia': 'Almería', 'Temperatura Max': '24.3',
                     'Hora(Temp Max)': '13:10', 'Temperatura Min': '13.1', 'Hora(Temp Min)': '13:10'})
writer.writerow({'Estacion Meteorologica': 'Herrera del Duque', 'Provincia': 'Badajoz', 'Temperatura Max': '28.1',
                     'Hora(Temp Max)': '16:40', 'Temperatura Min': '9.0', 'Hora(Temp Min)': '16:40'})
writer.writerow({'Estacion Meteorologica': 'Peraleda del Zaucejo', 'Provincia': 'Badajoz', 'Temperatura Max': '26.9',
                     'Hora(Temp Max)': '16:50', 'Temperatura Min': '9.3', 'Hora(Temp Min)': '16:50'})
writer.writerow({'Estacion Meteorologica': 'Coruña del Conde', 'Provincia': 'Burgos', 'Temperatura Max': '19.9',
                     'Hora(Temp Max)': '15:50', 'Temperatura Min': '5.0', 'Hora(Temp Min)': '15:50'})
writer.writerow({'Estacion Meteorologica': 'Aranda de Duero', 'Provincia': 'Burgos', 'Temperatura Max': '19.1',
                     'Hora(Temp Max)': '14:40', 'Temperatura Min': '4.7', 'Hora(Temp Min)': '14:40'})
writer.writerow({'Estacion Meteorologica': 'Valsequillo', 'Provincia': 'Córdoba', 'Temperatura Max': '26.7',
                     'Hora(Temp Max)': '15:50', 'Temperatura Min': '7.6', 'Hora(Temp Min)': '15:50'})
writer.writerow({'Estacion Meteorologica': 'Hinojosa del Duque', 'Provincia': 'Córdoba', 'Temperatura Max': '25.3',
                     'Hora(Temp Max)': '16:20', 'Temperatura Min': '10.1', 'Hora(Temp Min)': '16:20'})
writer.writerow({'Estacion Meteorologica': 'Granada-Cartuja', 'Provincia': 'Granada', 'Temperatura Max': '29.4',
                     'Hora(Temp Max)': '16:50', 'Temperatura Min': '11.9', 'Hora(Temp Min)': '16:50'})
writer.writerow({'Estacion Meteorologica': 'Granada Aeropuerto', 'Provincia': 'Granada', 'Temperatura Max': '29.3',
                     'Hora(Temp Max)': '17:50', 'Temperatura Min': '5.7', 'Hora(Temp Min)': '17:50'})
writer.writerow({'Estacion Meteorologica': 'Haro', 'Provincia': 'La Rioja', 'Temperatura Max': '17.8',
                     'Hora(Temp Max)': '15:50', 'Temperatura Min': '10.2', 'Hora(Temp Min)': '15:50'})
writer.writerow({'Estacion Meteorologica': 'Anguiano', 'Provincia': 'La Rioja', 'Temperatura Max': '13.6',
                     'Hora(Temp Max)': '15:00', 'Temperatura Min': '6.2', 'Hora(Temp Min)': '15:00'})
writer.writerow({'Estacion Meteorologica': 'Aranjuez', 'Provincia': 'Madrid', 'Temperatura Max': '25.1',
                     'Hora(Temp Max)': '16:30', 'Temperatura Min': '6.5', 'Hora(Temp Min)': '16:30'})
writer.writerow({'Estacion Meteorologica': 'Rascafría', 'Provincia': 'Madrid', 'Temperatura Max': '24.3',
                     'Hora(Temp Max)': '15:20', 'Temperatura Min': '3.5', 'Hora(Temp Min)': '15:20'})
writer.writerow({'Estacion Meteorologica': 'Estepona', 'Provincia': 'Málaga', 'Temperatura Max': '22.0',
                     'Hora(Temp Max)': '15:20', 'Temperatura Min': '13.3', 'Hora(Temp Min)': '15:20'})
writer.writerow({'Estacion Meteorologica': 'Marbella', 'Provincia': 'Málaga', 'Temperatura Max': '21.6',
                     'Hora(Temp Max)': '17:10', 'Temperatura Min': '15.8', 'Hora(Temp Min)': '17:10'})
writer.writerow({'Estacion Meteorologica': 'Pedraza', 'Provincia': 'Segovia', 'Temperatura Max': '18.2',
                     'Hora(Temp Max)': '17:00', 'Temperatura Min': '4.5', 'Hora(Temp Min)': '17:00'})
writer.writerow({'Estacion Meteorologica': 'Cuéllar', 'Provincia': 'Segovia', 'Temperatura Max': '21.2',
                     'Hora(Temp Max)': '14:50', 'Temperatura Min': '2.3', 'Hora(Temp Min)': '14:50'})
writer.writerow({'Estacion Meteorologica': 'Lora de Estepa', 'Provincia': 'Sevilla', 'Temperatura Max': '25.8',
                     'Hora(Temp Max)': '14:10', 'Temperatura Min': '2.3', 'Hora(Temp Min)': '14:10'})
writer.writerow({'Estacion Meteorologica': 'Écija', 'Provincia': 'Sevilla', 'Temperatura Max': '29.8',
                     'Hora(Temp Max)': '16:40', 'Temperatura Min': '8.9', 'Hora(Temp Min)': '16:40'})
writer.writerow({'Estacion Meteorologica': 'Ademuz', 'Provincia': 'Valencia', 'Temperatura Max': '21.7',
                     'Hora(Temp Max)': '16:50', 'Temperatura Min': '7.6', 'Hora(Temp Min)': '16:50'})
writer.writerow({'Estacion Meteorologica': 'Chelva', 'Provincia': 'Valencia', 'Temperatura Max': '23.8',
                     'Hora(Temp Max)': '16:10', 'Temperatura Min': '9.9', 'Hora(Temp Min)': '16:10'})

f.close()


# Una vez creadoel archivo lo podemos leer mediante este código:

# f = open('tiempo.csv')
# reader = csv.reader(f)
# for row in reader:
#    print(row)

#f.close()

