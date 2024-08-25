
""" Los métodos de cadena forman parte del tipo str. 
Esto significa que los métodos existen como variables de cadena o directamente como parte de la cadena. 
Por ejemplo, el método .title() devuelve la cadena en mayúsculas y se puede usar directamente con una cadena:
"""
print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

#División de una cadena
""" Un método de cadena común es .split(). Sin argumentos, el método separará la cadena en cada espacio. Esto crearía una lista de todas las palabras o números separados por un espacio: """

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
Salida: ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

""" En este ejemplo, trabaja con varias líneas, por lo que el carácter de nueva línea (implícito) se puede usar para dividir la cadena al final de cada línea, y crear líneas únicas: """

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
Salida: ['Daylight: 260 F', 'Nighttime: -280 F']


