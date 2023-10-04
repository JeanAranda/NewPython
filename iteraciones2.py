#Bucle for de Python
administrativos = ['Dayana','Tessy','Jean Pierre']
for stadmin in administrativos:
    print(stadmin)

#Iterables
#En Python, un iterable es un objeto que se puede utilizar en un bucle definido. 
#Si un objeto es iterable significa que se puede pasar como argumento a la función iter. 
#El iterable que se pasa como parámetro a la función iter
#regresa un iterator.
iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario