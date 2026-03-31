import random

class Minimax:
    def __init__(self, profundidad_maxima=4):
        # Cuántos turnos en el futuro va a predecir. 
        # (Ojo: ¡Más de 5 o 6 puede hacer que tu compu empiece a pensar muy lento!)
        self.profundidad_maxima = profundidad_maxima

    def evaluar_distancia(self, pos_gato, pos_raton, tablero):
        # 1. Calculamos la distancia base
        distancia = abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])
        
        # 2. Heurística de Acorralamiento: ¿Cuántas salidas tiene el ratón?
        salidas_raton = len(tablero.obtener_movimientos_validos(pos_raton[0], pos_raton[1]))
        
        # Sumamos un pequeño decimal basado en sus rutas de escape.
        # Si la distancia es igual (ej. 2), el gato (que busca minimizar) preferirá
        # un puntaje de 2.2 (ratón arrinconado con 2 salidas) antes que 2.4 (ratón en el centro con 4 salidas).
        return distancia + (salidas_raton * 0.1)

    def algoritmo_minimax(self, tablero, pos_gato, pos_raton, profundidad, es_turno_gato):
        # 1. CASO BASE: ¡Nota que ahora le pasamos el 'tablero' a la función evaluar_distancia!
        if profundidad == 0 or pos_gato == pos_raton:
            return self.evaluar_distancia(pos_gato, pos_raton, tablero)

        # 2. TURNO DEL GATO (Busca el número MENOR - Minimizar)
        # ... (El resto de esta función y todo lo de abajo se queda exactamente igual que como lo tenías) ...
        # 2. TURNO DEL GATO (Busca el número MENOR - Minimizar)
        if es_turno_gato:
            mejor_puntaje = float('inf')
            # Simulamos todos los movimientos posibles del gato en esta posición imaginaria
            movimientos = tablero.obtener_movimientos_validos(pos_gato[0], pos_gato[1])
            
            for mov in movimientos:
                # Llamada recursiva: movemos al gato y le pasamos el turno al ratón
                puntaje = self.algoritmo_minimax(tablero, mov, pos_raton, profundidad - 1, False)
                mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

        # 3. TURNO DEL RATÓN (Busca el número MAYOR - Maximizar)
        else:
            mejor_puntaje = float('-inf')
            # Simulamos todos los movimientos posibles del ratón
            movimientos = tablero.obtener_movimientos_validos(pos_raton[0], pos_raton[1])
            
            for mov in movimientos:
                # Llamada recursiva: movemos al ratón y le pasamos el turno al gato
                puntaje = self.algoritmo_minimax(tablero, pos_gato, mov, profundidad - 1, True)
                mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje

    def decidir_mejor_movimiento(self, tablero, personaje_actual, oponente):
            es_gato = type(personaje_actual).__name__.lower() == 'cat'
            
            # En lugar de guardar un solo mejor movimiento, guardaremos una LISTA de los mejores
            mejores_movimientos = []
            
            pos_actual = (personaje_actual.columna, personaje_actual.fila)
            pos_oponente = (oponente.columna, oponente.fila)

            movimientos_reales = tablero.obtener_movimientos_validos(pos_actual[0], pos_actual[1])

            if es_gato:
                mejor_puntaje = float('inf')
                for mov in movimientos_reales:
                    puntaje = self.algoritmo_minimax(tablero, mov, pos_oponente, self.profundidad_maxima - 1, False)
                    
                    # Si encontramos un puntaje ESTRICTAMENTE mejor, vaciamos la lista y ponemos este
                    if puntaje < mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejores_movimientos = [mov]
                    # Si el puntaje es IGUAL al mejor que ya teníamos, lo sumamos a las opciones
                    elif puntaje == mejor_puntaje:
                        mejores_movimientos.append(mov)
            else:
                mejor_puntaje = float('-inf')
                for mov in movimientos_reales:
                    puntaje = self.algoritmo_minimax(tablero, pos_oponente, mov, self.profundidad_maxima - 1, True)
                    
                    # Si encontramos un puntaje ESTRICTAMENTE mejor, vaciamos la lista y ponemos este
                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejores_movimientos = [mov]
                    # Si el puntaje es IGUAL al mejor que ya teníamos, lo sumamos a las opciones
                    elif puntaje == mejor_puntaje:
                        mejores_movimientos.append(mov)

            # Si por algún motivo no hay movimientos (arrinconado), devolvemos la posición actual
            if not mejores_movimientos:
                return pos_actual

            # ¡EL TRUCO DE MAGIA! Elegimos al azar entre todas las rutas que empataron con el mejor puntaje
            return random.choice(mejores_movimientos)