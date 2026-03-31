class Tablero:  
    def __init__(self,filatab,columnatab):
        self.filatab=filatab
        self.columnatab=columnatab
        self.matriz=[['-' for _ in range (columnatab)] for _ in range (filatab)]
    def dimension(self):#Imprimimos la matriz
        print("\n----Tablero---")
        for filatab in self.matriz:
            print(" [ " + "   " .join(filatab) + " ] ")

    def obtener_movimientos_validos(self, columna, fila):
        movimientos = []
        if fila > 0: 
            movimientos.append((columna, fila - 1)) # Mover Arriba
        if fila < self.filatab - 1: 
            movimientos.append((columna, fila + 1)) # Mover Abajo
        if columna > 0: 
            movimientos.append((columna - 1, fila)) # Mover Izquierda
        if columna < self.columnatab - 1: 
            movimientos.append((columna + 1, fila)) # Mover Derecha
        return movimientos        

        
    

