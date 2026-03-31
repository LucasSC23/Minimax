from tablero import Tablero #Importo mi tablero de la clase tablero
from clases import mouse, cat

mi_tablero=Tablero(5,5)#Dimensionamos nuestro tablero
mi_gato= cat(0,0)#Posicionamos al gato en su ubicacion inicial
mi_raton=mouse(4,4)#Posicionamos al raton en su ubicacion inicial


vidas= 7#Numero de veces que jugara 
while True: 
    #Por cada turno restamos las vidas
    vidas -= 1
    #Jugamos mientras sea verdadera la condicion: numero de vidas !0
    if vidas != 0:
        print(f"le quedan: {vidas} vidas ")
    else:
        print("el gato y el raton se quedaron sin vidas")    
        break    
    

    #Colocamos al gato y al raton dentro de la matriz
    mi_tablero.matriz=[[mi_gato.columna][mi_gato.fila]]= 'G'
    mi_tablero.matriz=[[mi_raton.columna][mi_raton.fila]]= 'R'
    mi_tablero.dimension()
    
    if mi_gato.atrapa(mi_raton):#Implementamos el metodo atrapa en el main
        print("\n----El gato gano----\n")
        break

    
