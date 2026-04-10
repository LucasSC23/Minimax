import random

class Minimax:
    def __init__(self, profundidad_maxima=4):
        self.profundidad_maxima = profundidad_maxima  # Turnos que predice hacia adelante

    def evaluar_distancia(self, pos_gato, pos_raton, tablero):
        # Distancia Chevyshev entre gato y ratón
        distancia = max(abs(pos_gato[0] - pos_raton[0]) , abs(pos_gato[1] - pos_raton[1]))
        # Salidas disponibles del ratón (acorralamiento)
        salidas = len(tablero.obtener_movimientos_validos(pos_raton[0], pos_raton[1]))
        # Distancia del ratón al queso
        dist_queso = abs(pos_raton[0] - tablero.pos_queso[0]) + abs(pos_raton[1] - tablero.pos_queso[1])
        # El gato minimiza → quiere distancia pequeña y pocas salidas
        # El ratón maximiza → quiere distancia grande y estar cerca del queso
        return distancia + (salidas * 0.1) - (dist_queso * 0.5)#Salidas, cuantas celdas de escape tiene el raton,dist_queso que tan lejos esta el queso

    def algoritmo_minimax(self, tablero, pos_gato, pos_raton, profundidad, es_turno_gato):
        # Caso base: sin profundidad o el gato atrapó al ratón  
        if profundidad == 0 or pos_gato == pos_raton:
            return self.evaluar_distancia(pos_gato, pos_raton, tablero)

        if es_turno_gato:  # El gato MINIMIZA
            mejor_puntaje = float('inf')
            for mov in tablero.obtener_movimientos_validos(pos_gato[0], pos_gato[1]):
                puntaje = self.algoritmo_minimax(tablero, mov, pos_raton, profundidad - 1, False)
                mejor_puntaje = min(mejor_puntaje, puntaje)          
            return mejor_puntaje
        else:              # El ratón MAXIMIZA
            mejor_puntaje = float('-inf')
            for mov in tablero.obtener_movimientos_validos(pos_raton[0], pos_raton[1]):
                puntaje = self.algoritmo_minimax(tablero, pos_gato, mov, profundidad - 1, True)
                mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje

    def decidir_mejor_movimiento(self, tablero, personaje, oponente, es_gato):
        pos_actual   = (personaje.fila, personaje.columna)
        pos_oponente = (oponente.fila,  oponente.columna)
        movimientos  = tablero.obtener_movimientos_validos(pos_actual[0], pos_actual[1])
        mejores      = []   # Lista de movimientos empatados en puntaje

        if es_gato:   # Gato: busca el movimiento con menor puntaje
            mejor_puntaje = float('inf')
            for mov in movimientos:
                p = self.algoritmo_minimax(tablero, mov, pos_oponente, self.profundidad_maxima - 1, False)
                if p < mejor_puntaje:
                    mejor_puntaje = p
                    mejores = [mov]
                elif p == mejor_puntaje:
                    mejores.append(mov)
        else:         # Ratón: busca el movimiento con mayor puntaje
            mejor_puntaje = float('-inf')
            for mov in movimientos:
                p = self.algoritmo_minimax(tablero, pos_oponente, mov, self.profundidad_maxima - 1, True)
                if p > mejor_puntaje:
                    mejor_puntaje = p
                    mejores = [mov]
                elif p == mejor_puntaje:
                    mejores.append(mov)

        # Si hay empate entre movimientos, elegimos uno al azar
        return random.choice(mejores) if mejores else pos_actual