import time
from os import system
import networkx as nx
import matplotlib.pyplot as plt

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
grafoCreado = False
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
        grafoCreado = True
        grafoCiudades = nx.DiGraph()
        nombresCiudades = []
        caminoCiudades = []
        valid = True

        while valid:
            try:
                cantidadCiudades = int(input('Cuantas ciudades desea ingresar?: '))
                valid = False
            except ValueError:
                valid = True
                print('\nPorfavor ingrese un valor numerico.\n')
        
        for x in range(cantidadCiudades):
            nombresCiudades.append(input(f'Ingrese el nombre de la ciudad {x+1}: '))
        
        print('\nAhora porfavor escriba las rutas existentes entre las ciudades: ')
        print('NOTA: Utilice el siguiente formato (Ciudad origen, Ciudad destino, Distancia en Km)\n')
        caminoExit = True
        while caminoExit:
            camino = []
            for i in range(2):
                camino.append(input(f'Ingrese el nombre de la ciudad {i+1}: '))
            camino.append(int(input('Cuantos kilometros tiene este camino?: ')))
            camino = tuple(camino)
            caminoCiudades.append(camino)

            respExit = input('Desea ingresar otro camino? s/n: ')
            if respExit.upper() == 'S':
                caminoExit = True
            else:
                caminoExit = False
        
        grafoCiudades.add_nodes_from(nombresCiudades)
        grafoCiudades.add_weighted_edges_from(caminoCiudades)
        
        time.sleep(PAUSE_DURATION)
    elif opcionMenuPrincipal == 3:
        if grafoCreado:
            origin = input('Porfavor ingrese la ciudad donde desea empezar: ')
            end = input('Ingrese la ciudad donde desea terminar: ')
            print(f'Todas las rutas para ir de {origin} hasta {end} son:')
            for path in nx.all_simple_paths(grafoCiudades, source=origin, target=end):
                print(path)
            input()
        else:
            print('Porfavor cree el grafo para poder obtener las rutas')
            time.sleep(PAUSE_DURATION)

    elif opcionMenuPrincipal == 4:
        if grafoCreado:
            origin = input('Porfavor ingrese la ciudad donde desea empezar: ')
            end = input('Ingrese la ciudad donde desea terminar: ')
            print(f'La ruta mas corta para ir de {origin} hasta {end} es:')
            print(*nx.shortest_path(grafoCiudades, source=origin, target=end, weight='weight'), sep=' -> ')
            input()
        else:
            print('Porfavor cree el grafo para poder obtener la ruta')
            time.sleep(PAUSE_DURATION)

    elif opcionMenuPrincipal == 5:
        if grafoCreado: 
            pos = nx.planar_layout(grafoCiudades)

            nx.draw_networkx_nodes(grafoCiudades, pos, node_size=700)
            nx.draw_networkx_edges(grafoCiudades, pos, width=2, edge_color='gray')

            nx.draw_networkx_labels(grafoCiudades, pos, font_size=15, font_family="sans-serif")

            edge_labels = nx.get_edge_attributes(grafoCiudades, "weight")
            nx.draw_networkx_edge_labels(grafoCiudades, pos, edge_labels)

            ax = plt.gca()
            ax.margins(0.08)
            plt.axis("off")
            plt.tight_layout()
            plt.show()
        else:
            print('Porfavor cree el grafo para poder imprimirlo graficamente')
            time.sleep(PAUSE_DURATION)

    elif opcionMenuPrincipal == 6:
        exit = False
    else:
        print('Porfavor escriba una de las opciones disponibles')
        time.sleep(PAUSE_DURATION)
        
