def limpiar_string(Pal):
	palmin = Pal.lowercase()
	pallimpio = palmin.replace(' ','').replace(',','').replace(';','').replace('.','').replace(':','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
	pallimpioygirado = pallimpio[::-1]
	return pallimpio


def comprobar_palindromo(paloriginal,palcomprobar):
	if paloriginal == palcomprobar:
		return true
	else:
		return false


PROGRAMA PRINCIPAL
palindromo = print("Por favor, introduce un palíndromo: ")

palcomprobar = limpiar_string(palíndromo)

comprobacion = comprobar_palindromo(palindromo,palcomprobar)

If comprobacion:
	print('¡Bien! La frase que has introducido es un palíndromo')
else:
	print('¡Lo siento! La frase que has introducido no es un palíndromo')