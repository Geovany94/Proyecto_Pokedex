import os

# os.system ("cls")

jugador = input('Por favor ingrese su nombre: ')

print("********** Pokemon ***********")

a = print("A = Bulbasaur") 
b=  print("B = Charmander ") 
c =  print("C = Squirtle ") 

eleccion = input('Escoga su Pokemon de Inicio, estos son los Disponibles: ')


while True:
    print (' ********** Menu Principal **********')
    print ('1 - Equipo Pokémon.')
    print ('2 - Batallas contra Pokémon salvajes')
    print ('4 - Pokédex.')
    print ('5 - Tienda.')
    print ('6 - Salir')
    opcion = int (input('Ingrese uns opción: '))
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        os.system ("cls")
        print ('1 - Atacar los puntos de salud de su oponente:')
        print ('2 - Capturar al Pokémon salvaje:')
        print ('4 - Utilizar un objeto curativo:')
        print ('4 - Huir del combate:')
        print ('5 - Salir: ')
        op = input("Ingrese la opcion: ")
        os.system("pause")
        os.system ("cls")

        if op == 5:
            break
        else:
            continue


    elif opcion == 5:
        os.system ("cls")
        print ('1 - Número en la Pokédex:')
        print ('2 - Nombre del Pokémon:')
        print ('3 - Si ha sido capturado por el entrenador:')
        print ('4 - Salir: ')
        op = input("Ingrese la opcion: ")
        os.system("pause")
        os.system ("cls")

        if op == 4:
            break
        else:
            continue

    elif opcion == 6:

     break
    else:
     continue
