def funcion_decoradora(funcion_parametro):

	def funcion_interior():
		# Acciones adicinales que decoran
		print('Vamos a realizar un calculo: ')

		funcion_parametro()

		# Acciones adicinales que docoran

		print('Hemos terminado el calculo')

	return funcion_interior


@funcion_decoradora
def suma():
	print(150 + 2220)


def resta():
	print(33 - 10)


suma()	
resta()