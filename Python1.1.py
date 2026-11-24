# En este apartado vas a ver ejercicios basicos de Python, el objetivo es
# que aprendas a manejar las herramientas que ofrece este lenguaje de programacion

# Primer taller: la funcion print
# Utiliza la funcion print() para imprimir la linea ¡Hola, Mundo! en la pantalla.
# Usa comillas dobles alrededor de la cadena.
# Habiendo hecho eso, usa la funcion print() nuevamente, 
# pero esta vez imprime tu nombre.
# Elimina las comillas dobles y ejecuta tu codigo. 
# Mira la reaccion de Python. ¿Que tipo de error arroja?
# Luego, elimina los parentesis, 
# vuelve a colocar las comillas dobles y ejecuta tu código nuevamente. 
# ¿Que tipo de error arroja esta vez?
# Experimenta todo lo que puedas. Cambia las comillas dobles a comillas simples, 
# usa multiples funciones print() en la misma linea, y luego en diferentes lineas. 
# Mira que pasa.

# Te dejo un ejemplo de print a continuación:

print("¡Hola, Mundo!")

# Segundo taller: Argumentos de palabra clave
# Modifica la primera línea de código en el editor, usando las palabras 
# claves reservadas sep y end, para que se obtenga la salida esperada. 
# Emplea dos funciones print() en el editor.

# No cambies nada en la segunda invocación del print().

# Esta es la salida esperada

# Programming***Essentials***in...Python

print("Programming","Essentials","in")
print("Python")

# Tercer taller: Uso de herramientas en el módulo

# Intenta:

# minimizar el número de invocaciones de la función print() 
# insertando \n en las cadenas;
# hacer que la flecha sea el doble de grande (pero mantener las proporciones)
# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: 
# una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá 
# "stringstring" 
# elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; 
# presta atención a dónde Python ve un error - 
# ¿es este el lugar donde realmente existe el error?
# haz lo mismo con algunos de los paréntesis;
# cambia cualquiera de las palabras print por otra cosa, 
# que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Taller 4. Código de producto
# Pasa "LIB", "2026" y "007" como tres argumentos a print().
# Usa sep= para obtener esta salida:
# LIB-2026-007


# Taller 5. Cuenta regresiva
# Usa dos llamadas a print().
# En la primera, pasa 3, 2 y 1 como argumentos separados.
# Usa sep= y end= en esa primera llamada para obtener:
# 3...2...1...¡Despegue!


# Taller 6. Lista de compras
# Usa una sola llamada a print() con una sola cadena.
# Coloca \n donde corresponda para obtener:
# Lista de compras
#
# - Pan
# - Leche
# - Huevos


# Taller 7. Tres filas iguales
# Usa una sola llamada a print().
# Repite la cadena "* * *\n" tres veces con * y usa end="".
# La salida debe ser:
# * * *
# * * *
# * * *


# Taller 8. Dibuja una bandera
# Usa una sola llamada a print() con tres argumentos.
# Forma cada fila repitiendo "#" o "-" ocho veces con *.
# Usa sep= con \n para colocar cada fila en su propia línea.
# Salida esperada:
# ########
# --------
# ########


# Taller 9. Insignia de Python
# Usa exactamente tres llamadas a print().
# Genera las filas de asteriscos multiplicando "*" por 10.
# Usa end= en la primera llamada para dejar una línea en blanco.
# En la segunda, pasa "★", "PYTHON" y "★" como argumentos
# separados y usa sep= para colocar un espacio entre ellos.
# Salida esperada:
# **********
#
# ★ PYTHON ★
# **********