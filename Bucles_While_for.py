""" Ahora que completó este módulo, puede:

Identificar cuándo se deben usar los bucles while y for.
Ejecutar una tarea varias veces mediante bucles while.
Recorrer en bucle los datos de la lista mediante bucles for. """

""" Un bucle while realiza una operación mientras (while, en inglés) una determinada condición es True. Puede usar un bucle while para lo siguiente:

Buscar otra línea en un archivo.
Comprobar si se ha establecido alguna marca.
Comprobar si un usuario ha terminado de introducir valores.
Comprobar si algo más ha cambiado para indicar que el código puede dejar de realizar la operación.
 Importante

Lo más importante que se debe recordar al crear bucles while es asegurarse de que cambia la condición. Si la condición siempre es True, Python seguirá ejecutando el código hasta que el programa se bloquee. """

#Sintaxis

#while <condition>:
    # code here


user_input = ''

#while user_input.lower() != 'done':
#    user_input = input('Enter a new value, or done when done')

    # Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')


""" Uso de bucles "for" con listas """

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

""" 
The first planet is  Mercury
The second planet is  Venus
The third planet is  Earth
"""


""" El bucle for es una instrucción con cinco partes importantes:

La palabra for, seguida de un espacio.
El nombre de la variable que quiere crear para cada valor de la secuencia (number).
La palabra in, entre espacios.
El nombre de la lista (countdown, en el ejemplo anterior) u objeto iterable que quiere recorrer en bucle, seguido de dos puntos (:).
El código que quiere ejecutar para cada elemento del objeto iterable, separado por espacios en blanco anidados. """


