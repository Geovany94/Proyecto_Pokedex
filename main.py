import os
from pila import Pila

#os.system ("cls")
#Crear pila para guardar pokemon en el equipo(max = 6)
equipo = Pila(6)
#Crear pila para guardar pokemon obtenidos (si equipo>6 )
equipomas6 = Pila()

id_jugador = input('Por favor ingrese su nombre: ')
print('Bienvenido ', id_jugador)
os.system('pause')
os.system ("cls")

print("********** Pokemon ***********")
print('Eliga un Pokemon para iniciar su aventura')
a =  print("A = Bulbasaur") 
b =  print("B = Charmander ") 
c =  print("C = Squirtle ") 

poke_inicial = ''

eleccion = input('Escoga su Pokemon de Inicio, estos son los Disponibles: ')
if eleccion == 'A' or eleccion == 'a':
    poke_inicial = 'Bulbasaur'
    print (f"Su nuevo pokemon es: {poke_inicial} ")
    equipo.ingresar_nuevo(2,poke_inicial, 'Juanito' , 2 , 999, 'planta', 
        'esquiva', 50, 10, 11, 15, 16, 'flash')
elif eleccion == 'B' or eleccion == 'b':
    poke_inicial = 'Charmander'
    print (f"Su nuevo pokemon es: {poke_inicial} ")
    equipo.ingresar_nuevo(2,poke_inicial, 'Juanito' , 2 , 999, 'planta', 
        'esquiva', 50, 10, 11, 15, 16, 'flash')
elif eleccion == 'C' or eleccion == 'c':
    poke_inicial = 'Squirtle'
    print (f"Su nuevo pokemon es: {poke_inicial} ")
    equipo.ingresar_nuevo(2,poke_inicial, 'Juanito' , 2 , 999, 'planta', 
        'esquiva', 50, 10, 11, 15, 16, 'flash')


while True:
    print (' ********** Menu Principal **********')
    print ('1 - Equipo Pokémon.')
    print ('2 - Batallas contra Pokémon salvajes')
    print ('3 - Pokédex.')
    print ('4 - Tienda.')
    print ('5 - Salir')
    opcion = int (input('Ingrese uns opción: '))
    if opcion == 1:
        equipo.ingresar_nuevo(45,'pikachu', 'Juanito' , 2 , 999, 'planta', 
        'esquiva', 50, 10, 11, 15, 16, 'flash')
        equipo.recorrer()
        print(equipo)
        os.system('pause')

    elif opcion == 2:
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

    elif opcion == 4:
        pass

    elif opcion == 5:
        break
    else:
     continue
