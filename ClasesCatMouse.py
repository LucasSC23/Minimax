from Tablero import Tablero

class Animal:
    def __init__(self, fila, columna, tablero):
        self.fila    = fila      # Fila actual del animal
        self.columna = columna   # Columna actual del animal
        self.tablero = tablero   # Referencia al tablero

    def mover(self, nueva_fila, nueva_columna):
        # Borramos la posición anterior en la matriz
        self.tablero.matriz[self.fila][self.columna] = '-'
        self.fila    = nueva_fila       # Actualizamos la fila
        self.columna = nueva_columna    # Actualizamos la columna

    def atrapa(self, otro):
        # Retorna True si ambos animales están en la misma celda
        return self.fila == otro.fila and self.columna == otro.columna

class Cat(Animal):
    pass   # Hereda todo de Animal, representa al gato

class Mouse(Animal):
    pass   # Hereda todo de Animal, representa al ratón