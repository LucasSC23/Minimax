from tablero import Tablero #Importo mi tablero de la clase tablero
from clases import mouse, cat
mi_tablero=Tablero(5,5)#Dimensionamos nuestro tablero
mi_gato= cat(0,0)
mi_raton=mouse(4,4)

#Colocamos al gato y al raton dentro de la matriz
mi_tablero.matriz=[[mi_gato.columna][mi_gato.fila]]= 'G'
mi_tablero.matriz=[[mi_raton.columna][mi_raton.fila]]= 'R'
mi_tablero.dimension()

