import sys
sys.stdout.reconfigure(encoding='utf-8')   # Permite tildes y caracteres especiales
import time
from Tablero import Tablero
from ClasesCatMouse import Cat, Mouse
from Minimax import Minimax

mi_tablero = Tablero(6, 6, pos_queso=(3, 3))   # Tablero 6x6, queso arriba a la derecha
mi_gato    = Cat(5, 0, mi_tablero)              # Gato: esquina inferior izquierda
mi_raton   = Mouse(5, 5, mi_tablero)            # Ratón: esquina inferior derecha
mi_ia      = Minimax(profundidad_maxima=4)      # IA con 4 niveles de predicción

# Dibujamos las posiciones iniciales en la matriz
mi_tablero.matriz[mi_gato.fila][mi_gato.columna]   = 'G'
mi_tablero.matriz[mi_raton.fila][mi_raton.columna] = 'R'

vidas          = 20       # Cantidad máxima de turnos
juego_termino  = False    # Bandera para controlar el fin del juego

while vidas > 0 and not juego_termino:
    vidas -= 1
    print(f"Turno restante: {vidas}")

    # --- Movimiento del GATO (minimiza) ---
    nueva_fila_g, nueva_col_g = mi_ia.decidir_mejor_movimiento(mi_tablero, mi_gato, mi_raton, es_gato=True)
    mi_gato.mover(nueva_fila_g, nueva_col_g)                        # Mueve y borra posición anterior
    mi_tablero.matriz[mi_gato.fila][mi_gato.columna] = 'G'          # Dibuja nueva posición

    if mi_gato.atrapa(mi_raton):                                    # ¿El gato atrapó al ratón?
        mi_tablero.dimension()
        print("*** El gato atrapo al raton! El gato gana. ***")
        juego_termino = True
        break

    # --- Movimiento del RATON (maximiza) ---
    nueva_fila_r, nueva_col_r = mi_ia.decidir_mejor_movimiento(mi_tablero, mi_raton, mi_gato, es_gato=False)
    mi_raton.mover(nueva_fila_r, nueva_col_r)                       # Mueve y borra posición anterior
    mi_tablero.matriz[mi_raton.fila][mi_raton.columna] = 'R'        # Dibuja nueva posición

    if mi_gato.atrapa(mi_raton):                                    # Verificamos captura tras mover ratón
        mi_tablero.dimension()
        print("*** El gato atrapo al raton! El gato gana. ***")
        juego_termino = True
        break

    # ¿El ratón llegó al queso?
    if (mi_raton.fila, mi_raton.columna) == mi_tablero.pos_queso:
        mi_tablero.dimension()
        print("*** El raton comio el queso! El raton gana. ***")
        juego_termino = True
        break

    mi_tablero.dimension()
    time.sleep(1)

if not juego_termino:
    print("*** Se acabaron los turnos. Empate! ***")