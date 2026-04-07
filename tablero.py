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
        movimientos = [
                (-1,-1)(0,-1)(1,-1)        
                (-1,0)       (1,0)      
                (-1,1) (0,1) (1,1)
        ]
    for dir_columna, dir_fila in movimientos:
        nueva_columna = columna + dir_columna
        nueva_fila = fila + dir_fila

    # Validamos que la nueva posición no se salga de los bordes del tablero
    if (0 <= nueva_columna < self.columnatab) and (0 <= nueva_fila < self.filatab):
        movimientos.append((nueva_columna, nueva_fila))

    

