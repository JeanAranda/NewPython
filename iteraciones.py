contador_externo = 0
contador_interno = 0
while contador_externo < 10:
    while contador_interno < 9:
        print(contador_externo, contador_interno)
        contador_interno +=1
        if contador_interno >= 5:
            break
    contador_externo +=1
    contador_interno = 0