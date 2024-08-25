""" Orden de las operaciones
Python respeta el orden de las operaciones en matemáticas. El orden de las operaciones determina que las expresiones se deben evaluar en este orden:

Paréntesis
Exponentes
Multiplicación y división
Suma y resta
"""

#SUMA

answer = 30 + 12
print(answer)

#RESTA

difference = 30 - 12
print(difference)

#MULTIPLICACION

product = 30 * 12
print(product)

#DIVISION

quotient = 30 / 12
print(quotient)

""" Conversión de cadenas en números """

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Output

#215
#215.3

""" Importante

Si usa un valor no válido para int o float, recibirá un error."""

"""Valores absolutos"""

print(39 - 16)
print(16 - 39)


""" Observe que la diferencia entre las dos ecuaciones es que los números se invierten. Las respuestas son 23 y -23, respectivamente. Al determinar la distancia entre dos planetas, no importa el orden en el que se escriben los números, ya que la respuesta absoluta es la misma.

Use abs para convertir el valor negativo en su valor absoluto. Si hace la misma operación mediante abs (e imprime las respuestas), verá que muestra 23 para ambas ecuaciones."""


print(abs(39 - 16))
print(abs(16 - 39))


#Output
#23
#23

""" Redondeo """

print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

#Output
#1
#2
#2
#3


"""
Biblioteca matemática
Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados. Una de las más comunes es la biblioteca math. math permite hacer el redondeo con floor y ceil, proporcionar el valor de pi y muchas otras operaciones. Veamos cómo usar esta biblioteca para redondear hacia arriba o hacia abajo.

El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor.

"""

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)


#Output
#13
#12
