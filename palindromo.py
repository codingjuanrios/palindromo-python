#IMPORT
import json
import random


#FUNCIONES

def limpiar_string(Pal):
	palmin = Pal.lower()
	pallimpio = palmin.replace(' ','').replace(',','').replace(';','').replace('.','').replace(':','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
	return pallimpio


def girar_palindromo(Pal):
	palgirado = Pal[::-1]
	return palgirado

def comprobar_palindromo(paloriginal,palcomprobar):
	if paloriginal == palcomprobar:
		return True
	else:
		return False

def palindromo_de_regalo():

	with open("listado.json", "r") as read_file:
    	listado = json.load(read_file)

    print("Muchas gracias por usar nuestro script")

    print("Aquí tiene un palíndromo de regalo:")

	print(random.choice(listado))


#PROGRAMA PRINCIPAL

programa = True

while programa:
	palindromo = input("Por favor, introduce un palíndromo: ")

	pallimpiado = limpiar_string(palindromo)

	palcomprobar = girar_palindromo(pallimpiado)

	comprobacion = comprobar_palindromo(pallimpiado,palcomprobar)

	if comprobacion:
		print('¡Bien! La frase que has introducido es un palíndromo')
	else:
		print('¡Lo siento! La frase que has introducido no es un palíndromo')

	continuar = input("¿Quieres seguir? (S/N): ")

	if continuar == "s" or continuar == "S":
		print("¡Vamos otra vez!")
	elif continuar == "n" or continuar == "N":
		print("¡Adios!")

		palindromo_de_regalo()

		programa = False

	else:
		print("No te he entendido, así que me las piro")

		palindromo_de_regalo()

		programa = False

quit()