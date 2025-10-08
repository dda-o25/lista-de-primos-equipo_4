"""

ANGELICA ELIZABETH IBARRA DIAZ
DIAZARTURO ARJONA HERMOSILLOA
CHRISTIAN ALONSO FLORES BURGOS
MARCO FABRIZIO AZPEITIA CASTELLANOS

10 de octubre 2025

Obtener la lista de todos los números primos menores a un número dado

"""

# Declaraciones

# Entradas
numero = int(input("Introduzca un número:"))
es_primo = True
cadena = []
#Proceso 
for i in range(2, numero):
    es_primo = True
    for x in range(2, i):
        if i % x == 0:
            es_primo = False
    if es_primo:
        cadena.append(i)
             
# Salidas
print(f"Los números primos menores o iguales a {numero} son: {cadena}")