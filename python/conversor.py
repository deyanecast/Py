#quetzales = input("Cuantos quetzales tienes?: ")
#quetzales = float(quetzales)
#valor_dolar = 7.70
#dolares = quetzales / valor_dolar
#dolares = round (dolares, 2)
#dolares = str(dolares)
#print("Tienes $" + dolares + " dolares")

def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")

menu = """
BIENVENIDO AL CONVERSOR DE MONEDA :3

1-PESOS COLOMBIANOS
2-PESOS ARGENTINOS 
3-PESOS MEXICANOS 

Elige una opcion:  """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else: 
    print('ingresa una opcion correcta :enojado:')





