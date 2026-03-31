class Minimax:
    def __init__(self):
        pass

    # Podemos agregar esto como un método independiente o dentro de una clase
    def calcular_distancia(gato, raton):
        distancia = abs(gato.columna - raton.columna) + abs(gato.fila - raton.fila)#abs es para utilizar el valor absoluto del numero
        return distancia
        

    def decidir_mejor_movimiento(self, tablero, personaje_actual, oponente):
        # ¡AQUÍ ESTARÁ LA MAGIA! 
        # Esta función analizará el tablero y devolverá la coordenada (columna, fila) perfecta.
        
        # Por ahora, solo obtenemos los movimientos válidos para que no dé error, 
        # y le decimos que tome el primer movimiento disponible como prueba.
        movimientos_posibles = tablero.obtener_movimientos_validos(personaje_actual.columna, personaje_actual.fila)
    
        if movimientos_posibles:
            return movimientos_posibles[0] # Retorna una tupla: (nueva_columna, nueva_fila)
        else:
            return (personaje_actual.columna, personaje_actual.fila) # Se queda quieto si no hay salida



  