#Ejemplo de un error de python
print("(print)Funcion que imprime las invoaciones colocadas o vacias")
#print(")
#print"")
#print""
#print)
#print(
#print"

#2.Caracteres de escape y nueva línea en Python
print("2.Caracteres de escape y nueva línea en Python")
#Esto es un salto de Linea \n
print("La araña se subio\na sU telaraña")
print()
print("La araña se subió\na su telaraña")
print()
print("Como se puede observar, aparecen dos nuevas líneas en la canción infantil, en los lugares donde se ha utilizado ('\ n'). el ejemplo es junto solo para que se pueda areciar como es lo separé")
print()
#Nota: Argumento en la funcion print es una cadena por el momento

print("La barra invertida (\) tiene un significado muy especial\
cuando se usa dentro de cadenas - se llama carácter de escape.")
print("La barra invertida (\) tiene un significado muy especial\ncuando se usa dentro de cadenas - se llama carácter de escape.")
print()
print("La palabra escape debe entenderse específicamente - significa que la serie de caracteres en la cadena se escapa por un momento (un momento muy breve) para introducir una inclusión especial.")
print()
#Nota: \t es para tabulaciones
print("En\totras palabras, la barra invertida no significa nada en sí misma, sino que es solo una especie de anuncio de que el siguiente carácter después de la barra invertida también tiene un significado diferente.\
\n\
La la letra n colocada después de la barra invertida proviene de la palabra newline.\
\t\n\
Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nuevalínea, que insta a la consola a iniciar una nuevalínea de salida.")
print()
print("Esta convención tiene dos consecuencias importantes:\
\n\
1. Si deseas colocar solo una barra invertida dentro de una cadena, no olvides su naturaleza de escape - tienes que duplicarla. Por ejemplo, una invocación como esta provocará un error:")
print("")
#print("\")
print("mientras que esta no lo hará:")
print("\\")
print()
#2.1.9 Usando múltiples argumentos
print("2.1.9 Usando múltiples argumentos")
print("Hasta ahora hemos probado el comportamiento de la función print() \n\
sin argumentos y con un argumento. También vale la pena intentar \n\
alimentar a la función print() con más de un argumento.\
\
Mira la ventana del editor. Esto es lo que vamos a probar ahora:")
print()
#Como ves hay comas y se  hace para unir varias cadenas
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")
print()
print("Hay una invocación de la función print(), pero contiene tres argumentos. Todos ellos son cadenas.\
\
Los argumentos están separados por comas.\n\
Los hemos rodeado de espacios para hacerlos más visibles, pero no es \t\trealmente necesario, y no lo haremos más.\
\
\nEn este caso, las comas al separar los argumentos juega un papel completamente diferente al de la coma dentro de la cadena. \nEl primero es parte de la sintaxis de Python, mientras que el segundo está diseñado para mostrarse en la consola.\
\nSi observas el código nuevamente, verás que hay no hay espacios dentro de las cadenas.\
\
\nEjecuta el código y ve qué sucede.\
\
\nLa consola ahora debería mostrar el siguiente texto:")
print()
#La Witsi Witsi Araña subió a su telaraña.
print("Los espacios, eliminados de las cadenas, han vuelto a aparecer. ¿Puedes explicar por qué?\
\n\
Dos conclusiones emergen de este ejemplo:\
\n\
La función print() invocada con más de un argumento los muestra todos en una sola línea.\
\nLa función print() pone un espacio entre los argumentos de salida por iniciativa propia.")

#2.1.10 Argumentos posicionales
print("\n2.1.10 Argumentos posicionales")
print("\nAhora que sabes un poco sobre las costumbres de la función print(), te mostraremos cómo cambiarlas.\
\
\nDeberías poder predecir la salida sin ejecutar el código en el editor.")
print("\nMi nombre es", "Python.")
print("Monty Python.")
print("\nLa forma en que estamos pasando los argumentos a la función print() es la más común en Python, y se llama la forma posicional.\
\nEste nombre proviene del hecho de que el significado del argumento está dictado por su posición (por ejemplo, el segundo argumento se\
\mostrará después del primero, no al revés).\
\
\nEjecuta el código y comprueba si el resultado coincide con tus predicciones.")

#2.1.11 Argumentos de palabra clave
print("\n2.1.11 Argumentos de palabra clave")
print("\nPython ofrece otro mecanismo para el paso de argumentos, que puede ser útil cuando deseas convencer a la función print() para que cambie un poco su comportamiento.\
\
\nNo vamos a explicarlo en profundidad ahora. Planeamos hacerlo cuando hablemos de funciones. Por ahora, simplemente queremos mostrarte cómo funciona. Siéntete libre de usarlo en tus propios programas.\
\n\
El mecanismo se llama argumentos de palabras clave. El nombre proviene del hecho de que el significado de estos argumentos se toma no de su ubicación (posición) sino de la palabra especial (palabra clave) utilizada para identificarlos.\
\n\
La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.\
\n\
En la ventana del editor puedes ver un ejemplo muy simple de cómo usar un argumento de palabra clave.")
#Recuerda para que sirve el end=""
print("\nMi nombre es", "Python.", end=" ")
print("Monty Python.")

#Atento a esto
print("\nPara usarlo, es necesario conocer algunas reglas:\
\
\nUn argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;\
cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)\
\nEn nuestro ejemplo, hemos utilizado el argumento de palabra clave end, y lo hemos configurado como cadena que contiene un espacio.\
\
\nEjecuta el código para ver cómo funciona.\
\
\nLa consola ahora debería estar mostrando el siguiente texto:")
print("\nya salio el texto...\nMi nombre es Python. Monty Python.")
print("\nComo puedes ver, el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.\
\
El comportamiento predeterminado refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente manera: end='\n'.\
\nY ahora es el momento de intentar algo más difícil.\
\
Si miras con atención, verás que hemos usado el argumento end, pero la cadena que se le asignó está vacía (no contiene ningún carácter).\
\
¿Qué sucederá ahora? Ejecuta el programa en el editor para averiguarlo.\
")
print("\nRecuerda que estas dos lineas de codigo te indica como funciona", end="\nSi quieres mira el codigo animate!!!")
print("\nMi nombre es", end="")
print("Monty Python.")
print("\nComo el argumento end se ha establecido a nada, la función print() tampoco genera nada, una vez que se han agotado sus argumentos posicionales.\
\nLa consola ahora debería mostrar el siguiente texto:")
#Mi nombre es Monty Python.
print("\nNota: no se han enviado líneas nuevas a la salida.\
\nLa cadena asignada al argumento de palabra clave end puede ser de cualquier longitud. Experimenta con él si quieres.\
\nDijimos anteriormente que la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.\
\nEl argumento de palabra clave que puede hacer esto se denomina sep (como en separador).\
\nMira el código en el editor, y ejecútalo.")
#Esta  linea de codigo te explica como se separa con el agumento sep
print("\nChequea el codigo para que veas como se separa")
print("El argumento (sep) produce los siguientes resultados:")
print("Mi","nombre","es","Monty","Python.", sep="***")
#Como ves se utiliza *** para el valor del argumento
print("\nLa función print() ahora usa un guión, en lugar de un espacio, para separar los argumentos de salida.\
\nNota: el valor del argumento sep también puede ser una cadena vacía. Pruébalo tu mismo.\
\nAmbos argumentos de palabra clave pueden mezclarse en una invocación, como aquí en la ventana del editor.")
#Mira este codidgo
print("\nEl resultado de dos argumentos.....")
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("\nEl ejemplo no tiene mucho sentido, pero presenta de forma visible las interacciones entre end y sep.\
\n¿Puedes predecir el resultado?\
\nEjecuta el código y comprueba si coincide con tus predicciones.\
\nAhora que comprendes la función print(), estás listo para considerar cómo almacenar y procesar datos en Python.\
\nSin print(), no podrías ver ningún resultado.")

#2.1.12   LAB   La función print() y sus argumentos
print("\n2.1.12   LAB   La función print() y sus argumentos")
print("\nEscenario\n\
Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, para que se obtenga la salida esperada. \nEmplea dos funciones print() en el editor.\
\nNo cambies nada en la segunda invocación del print().\n\
\nSalida Esperada\
\nProgramming***Essentials***in...Python")
#Separado con comas
print("\nEl sigiente  codigo es el que debes modificar para que se vea igual al de la salida")
print("Programming","Essentials","in")
print("Python")
print("\nEs hora de demostrar lo que aprendiste...")
#Este es el ejemlo que ya se entendio
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

#2.1.13   LAB   Dando formato a la salida
print("\n2.1.13   LAB   Dando formato a la salida")

print("\nEsceneario\
\nTe recomendamos encarecidamente que juegues con el código que hemos escrito para y realiza algunos (quizás incluso destructivos) cambios.\
\nSiéntete libre de modificar cualquier parte del código, pero hay una condición - aprende de tus errores y saca tus propias conclusiones.\
\nIntenta:\
\nMinimizar el número de invocaciones de la función print() insertando \nen las cadenas;",end="\nhacer que la flecha sea el doble\
 de grande (pero mantener las proporciones, duplica la flecha, colocando ambas flechas una al lado de la otra;")
#duplica la flecha, colocando ambas flechas una al lado de la otra;\
#nnota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
#duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
#elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
#haz lo mismo con algunos de los paréntesis;
#cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
#reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.
########################################################################################
print()
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("JOT   APE")
print("  *   *")
print("  *   *")
print("  Hoola")
##################
# Sample Solution

###################
print("\noriginal version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################

print()
# Sample Solution

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)


#2.1.14 RESUMEN DE SECCIÓN
texto = """\n
1. La función print() es una función integrada imprime/envía un mensaje específico a la pantalla/ventana de consola.

2. Las funciones integradas, al contrario de las funciones definidas por el usuario, están siempre disponibles y no tienen que ser importadas. Python 3.7.1 viene con 69 funciones incorporadas. Puedes encontrar su lista completa en orden alfabético en Python Standard Library.

3. Para llamar a una función (invocación de función), debe utilizarse el nombre de la función seguido de un paréntesis. Puedes pasar argumentos a una función colocándolos dentro de los paréntesis. Se deben separar los argumentos con una coma, por ejemplo, print("¡Hola,", "Mundo!"). Una función print() "vacía" imprime una línea vacía a la pantalla.

4. Las cadenas de Python están delimitadas por comillas, por ejemplo, "Soy una cadena" (comillas dobles), o 'Yo soy una cadena, también' (comillas simples).

5. Los programas de computadora son colecciones de instrucciones. Una instrucción es un comando para realizar una tarea específica cuando se ejecuta, por ejemplo, para imprimir un determinado mensaje en la pantalla.

6. En las cadenas de Python la barra diagonal inversa (\) es un carácter especial que anuncia que el siguiente carácter tiene un significado diferente, por ejemplo, \n (el carácter de nuevalínea) comienza una nuevalínea de salida.

7. Los argumentos posicionales son aquellos cuyo significado viene dictado por su posición, por ejemplo, el segundo argumento se emite después del primero, el tercero se emite después del segundo, etc.

8. Los argumentos de palabra clave son aquellos cuyo significado no está dictado por su ubicación, sino por una palabra especial (palabra clave) que se utiliza para identificarlos.

9. Los parámetros end y sep se pueden usar para dar formato la salida de la función print(). El parámetro sep especifica el separador entre los argumentos emitidos. Por ejemplo, print("H", "E", "L", "L", "O", sep="-"), mientras que el parámetro end especifica que imprimir al final de la declaración de impresión.
"""

print(texto)

#2.1.15 CUESTIONARIO DE SECCIÓN
print("\n2.1.15 CUESTIONARIO DE SECCIÓN")
pregunta1 = '''\nPregunta 1: ¿Cuál es la salida del siguiente programa?
print("Mi\\nnombre\\nes\\nBond.", end=" ")
print("James Bond.")'''
print(pregunta1)
#Atento a la solución
print("\nLa solucion de la salida es:...")
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")
pregunta2 = '''\nPregunta 2: ¿Cuál es la salida del siguiente programa?
print(sep="&", "fish", "chips")
'''
print(pregunta2,"\nSale error ")
salida2 = ''' File "main.py", line 1
    print(sep="&", "fish", "chips")
                  ^
SyntaxError: positional argument follows keyword argument'''
print(salida2)
print("\nRecuerda: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.")
pregunta3 = '''Pregunta 3: ¿Cuál de las siguientes print() invocaciones de función generarán un SyntaxError?
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')'''
print(pregunta3, "\nLa línea 5 generará un SyntaxError, porque el símbolo ' en la cadena Greg's book. requiere un carácter de escape.")
print("Greg\'s book.")
