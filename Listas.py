"""
Después de completar este módulo, podrá:

Identificar cuándo se debe usar una lista.
Crea una lista.
Acceder a un elemento determinado de una lista mediante índices.
Insertar elementos al final de una lista.
Ordenar y segmentar una lista.

"""
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

#Output
#The first planet is Mercury
#The second planet is Venus
#The third planet is Earth

"""Nota

Dado que todos los índices empiezan por 0, [1] es el segundo elemento, [2] es el tercero, etc."""


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

#Salida: Mars is also known as Red Planet

"""Determinación de la longitud de una lista"""

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

#Salida: There are 8 planets in the solar system

""" Incorporación de valores a listas """

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

#Salida: There are actually 9 planets in the solar system.


"""  Eliminación de valores de listas  """

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

#Salida: No, there are definitely 8 planets in the solar system.

""" Uso de índices negativos """

print("The first planet is", planets[0])

#Salida: The first planet is Mercury

"""Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.

En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo."""

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

#Output
#The last planet is Neptune
#The penultimate planet is Uranus

"""  Búsqueda de un valor en una lista """

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

#Salida: Jupiter is the 5 planet from the sun

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")

#Salida: Mercury is the 1 planet from the sun


""" Trabajo con números en listas """

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

#Output
#On Earth, a double-decker bus weighs 124054 N
#On Mercury, a double-decker bus weighs 46892.4 N

""" Uso de min() y max() con listas """

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

#Salida:The lightest a bus would be in the solar system is 46768.358 N
#       The heaviest a bus would be in the solar system is 292767.44 N

""" Segmentación de listas """

""" Combinación de listas """

""" Ordenación de listas """