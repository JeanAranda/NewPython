#2.2 Sección 2 – Literales de Python
print("*"*80)
print("2.2 Sección 2 – Literales de Python\nBienvenido a la Sección 2, donde hablaremos sobre los literales de Python.")
print("*"*80)
texto = '''\n2.2.1 Literales - los datos en sí mismos

Ahora que tienes un poco de conocimiento acerca de algunas de las poderosas características que ofrece la función print(), es tiempo de aprender sobre cuestiones nuevas, y un nuevo término - el literal.

Un literal se refiere a datos cuyos valores están determinados por el literal mismo.

Debido a que es un concepto un poco difícil de entender, un buen ejemplo puede ser muy útil.

Observa los siguientes dígitos:

123
¿Puedes adivinar qué valor representa? Claro que puedes - es ciento veintitrés.

Que tal este:

c
¿Representa algún valor? Tal vez. Puede ser el símbolo de la velocidad de la luz, por ejemplo.\
\nTambién puede representar la constante de integración. Incluso la longitud de una hipotenusa en el Teorema de Pitágoras.
\nExisten muchas posibilidades.

No se puede elegir el valor correcto sin algo de conocimiento adicional.

Y esta es la pista: 123 es un literal, y c no lo es.

Se utilizan literales para codificar datos y ponerlos dentro del código. Ahora mostraremos algunas convenciones que se deben seguir al utilizar Python.

Comencemos con un sencillo experimento - observa el fragmento de código en el editor.
print("2")
print(2)\nSalida del codigo'''

print(texto)
print("2")
print(2)

texto='''\nLa primera línea luce familiar. La segunda parece ser errónea debido a la falta visible de comillas.

Intenta ejecutarlo.

Si todo salió bien, ahora deberías de ver dos líneas idénticas.

¿Qué paso? ¿Qué significa?

A través de este ejemplo, encuentras dos tipos diferentes de literales:

Una cadena, la cual ya conoces,
Y un número entero, algo completamente nuevo.
La función print() los muestra exactamente de la misma manera - Sin embargo, internamente, la memoria de la
computadora los almacena de dos maneras completamente diferentes - La cadena existe como eso solo una cadena - una serie de letras.

El número es convertido a una representación máquina (una serie de bits). La función print() es capaz de mostrar ambos en una forma legible para humanos.

Vamos a tomar algo de tiempo para discutir literales numéricas y su vida interna.'''
print(texto)

texto='''\n2.2.2 Enteros
Quizá ya sepas un poco acerca de como las computadoras hacen cálculos con números. Tal vez has escuchado del sistema binario, y como es que ese es el sistema que las computadoras utilizan para almacenar números y como es que pueden realizar cualquier tipo de operaciones con ellos.

No exploraremos las complejidades de los sistemas numéricos posicionales, pero se puede afirmar que todos los números manejados por las computadoras modernas son de dos tipos:

enteros, es decir, aquellos que no tienen una parte fraccionaria,
y números punto-flotantes (o simplemente flotantes), los cuales contienen (o son capaces de contener) una parte fraccionaría.
Esta definición no es tan precisa, pero es suficiente por ahora. La distinción es muy importante, y la frontera entre estos dos tipos de números es muy estricta. Ambos tipos difieren significativamente en como son almacenados en una computadora y en el rango de valores que aceptan.

La característica del valor numérico que determina el tipo, rango y aplicación se denomina el tipo.

Si se codifica un literal y se coloca dentro del código de Python, la forma del literal determina la representación (tipo) que Python utilizará para almacenarlo en la memoria.

Por ahora, dejemos los números flotantes a un lado (regresaremos a ellos pronto) y analicemos como es que Python reconoce un número entero.

El proceso es casi como usar lápiz y papel - es simplemente una cadena de dígitos que conforman el número. pero hay una condición - no se deben insertar caracteres que no sean dígitos dentro del número.

Tomemos por ejemplo, el número once millones ciento once mil ciento once. Si tomaras ahorita un lápiz en tu mano, escribirías el siguiente número: 11,111,111, o así: 11.111.111, incluso de esta manera: 11 111 111.

Es claro que la separación hace que sea más fácil de leer, especialmente cuando el número tiene demasiados dígitos. Sin embargo, Python no acepta estas cosas, está prohibido. ¿Qué es lo que Python permite?. El uso de guion bajo en los literales numéricos.*

Por lo tanto, el número se puede escribir ya sea así: 11111111, o como sigue: 11_111_111.

  Nota     *Python 3.6 ha introducido el guion bajo en los literales numéricos, permitiendo colocar un guion bajo entre dígitos y después de especificadores de base para mejorar la legibilidad. Esta característica no está disponible en versiones anteriores de Python.

¿Cómo se codifican los números negativos en Python? Como normalmente se hace, agregando un signo de menos. Se puede escribir: -11111111, o -11_111_111.

Los números positivos no requieren un signo positivo antepuesto, pero es permitido, si se desea hacer. Las siguientes líneas describen el mismo número: +11111111 y 11111111.'''
print(texto)
