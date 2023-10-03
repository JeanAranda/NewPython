nom_usu1 = input('Coloca el nombre del primer usuario: ')
nom_usu2 = input('Coloca el nombre del segundo usuario: ')
usu_1 = int(input(f'Coloca la edad de {nom_usu1}: '))
usu_2 = int(input(f'Coloca la edad de {nom_usu2}: '))

if usu_1 > usu_2:
    print(f'La edad de {nom_usu1}, es mayor que {nom_usu2}')
elif usu_1 < usu_2:
    print(f'La edad de {nom_usu2}, es mayor que {nom_usu1}')
else:
    print(f'La edad de {nom_usu1} y {nom_usu2}, son iguales.')