class Tablero:
    def __init__(self, filatab, columnatab, pos_queso=(0, 5)):
        self.filatab = filatab          # Cantidad de filas del tablero
        self.columnatab = columnatab    # Cantidad de columnas del tablero
        self.pos_queso = pos_queso      # Posición del queso (fila, columna)
        # Creamos la matriz llena de '-' (casillas vacías)
        self.matriz = [['-' for _ in range(columnatab)] for _ in range(filatab)]
        # Colocamos el queso en la matriz
        self.matriz[pos_queso[0]][pos_queso[1]] = 'Q'

    def dimension(self):
        print("\n--- Tablero ---")
        for fila in self.matriz:
            print(" [ " + "  ".join(fila) + " ] ")

    def obtener_movimientos_validos(self, fila, columna):
        # Las 8 direcciones posibles (horizontal, vertical y diagonal)
        movimientos = [
            (-1,-1), (-1, 0), (-1, 1),
            ( 0,-1),          ( 0, 1),
            ( 1,-1), ( 1, 0), ( 1, 1)
        ]
        validos = []
        for dir_fila, dir_columna in movimientos:
            nueva_fila    = fila    + dir_fila      # Calculamos la nueva fila
            nueva_columna = columna + dir_columna   # Calculamos la nueva columna
            # Solo agregamos si no se sale del tablero
            if (0 <= nueva_fila < self.filatab) and (0 <= nueva_columna < self.columnatab):
                validos.append((nueva_fila, nueva_columna))
        return validos
