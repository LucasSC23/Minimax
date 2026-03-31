from Tablero import Tablero #Importo mi tablero de la clase tablero
from ClasesCatMouse import mouse, cat
from Minimax import Minimax

mi_tablero=Tablero(6,6)#Dimensionamos nuestro tablero
mi_gato= cat(0,0)#Posicion inicial: gato
mi_raton=mouse(4,4)#Posicion inicial: raton
mi_ia_minimax=Minimax()


vidas= 7#Numero de veces que jugara 
while True: 
    #Por cada turno restamos las vidas
    vidas -= 1
    #Jugamos mientras sea verdadera la condicion: numero de vidas !0
    if vidas != 0:
        print(f"Le quedan: {vidas} vidas ")
    else:
        print("El gato y el raton se quedaron sin vidas")    
        break    
    

    #Se borra la posicion anterior del gato y del raton   
    mi_tablero.matriz[mi_gato.columna][mi_gato.fila]= '-' 
    mi_tablero.matriz[mi_raton.columna][mi_raton.fila]= '-'
    
    
    # 1. Recibes y repartes los valores (Desempaquetado)
    nueva_col_gato, nueva_fil_gato = mi_ia_minimax.decidir_mejor_movimiento(mi_tablero, mi_gato, mi_raton)

    # 2. Los usas para actualizar al objeto real
    mi_gato.columna = nueva_col_gato
    mi_gato.fila = nueva_fil_gato
    #Colocamos al raton en su nueva ubicacion en la matriz
    mi_tablero.matriz[mi_gato.columna][mi_gato.fila]= 'G'


    
    # 1. Recibes y repartes los valores (Desempaquetado)
    nueva_col_raton, nueva_fil_raton = mi_ia_minimax.decidir_mejor_movimiento(mi_tablero, mi_gato, mi_raton)

    # 2. Los usas para actualizar al objeto real
    mi_raton.columna = nueva_col_raton
    mi_raton.fila = nueva_fil_raton

    #Colocamos al raton en su nueva ubicacion en la matriz
    mi_tablero.matriz[mi_raton.columna][mi_raton.fila]= 'R'





    mi_tablero.dimension()
    
    if mi_gato.atrapa(mi_raton):#Implementamos el metodo atrapa en el main
        print("\n----El gato gano🐱----\n")
        break

    
