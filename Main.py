import time
from os import system

def obtenerOpcion():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce una de las opciones disponibles')

    return num

PAUSE_DURATION = 2.5
exit = True
while exit:
    system('cls')
    print('BIENVENIDO/A A NUESTRA APLICACION DE UN GRAFO')
    print('1. Hoja de presentación')
    print('2. Crear red de ciudades')
    print('3. Ruta entre ciudades')
    print('4. Ruta a partir de una ciudad a otra')
    print('5. Imprimir graficamente')
    print('6. Salir')

    opcionMenuPrincipal = obtenerOpcion()

    if opcionMenuPrincipal == 1:
        system("cls")
        print("                   UNIVERSIDAD TECNOLOGICA DE PANAMA")
        print("          FACULTAD DE INGENIERIA DE SISTEMAS COMPUTACIONALES")
        print("         DEPARTAMENTO DE COMPUTACION Y SIMULACION DE SISTEMAS")
        print("")
        print("                LIC. EN ING. SISTEMAS Y COMPUTACION")
        print("                      ESTRUCTURAS DE DATOS II")
        print("")
        print("                         APLICACIONES DE LOS GRAFOS")
        print("")
        print("Prof. Yolanda de Miguelena                  Integrantes: Cesar Garzon")
        print("                                                         Kevin Rodriguez")
        print("                                                         Johan Pimentel")
        print("                                                         Gabriel Nunez")
        print("")
        print("                            Grupo: 1IL124")
        print("")
        print("                        FECHA: 26 / Oct / 2022")

        input()
    elif opcionMenuPrincipal == 2:
        print('Crear red de ciudades')
        time.sleep(PAUSE_DURATION)
    elif opcionMenuPrincipal == 3:
        print('Ruta entre ciudades')
        time.sleep(PAUSE_DURATION)
    elif opcionMenuPrincipal == 4:
        print('Ruta a partir de una ciudad a otra')
        time.sleep(PAUSE_DURATION)
    elif opcionMenuPrincipal == 5:
        print('Imprimir graficamente')
        time.sleep(PAUSE_DURATION)
    elif opcionMenuPrincipal == 6:
        exit = False
    else:
        print('Porfavor escriba una de las opciones disponibles')
        time.sleep(PAUSE_DURATION)
        