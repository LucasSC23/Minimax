class Tablero:  
    def __init__(self,filatab,columnatab):
        self.filatab=filatab
        self.columnatab=columnatab
        self.matriz=[['-' for _ in range (columnatab)] for _ in range (filatab)]
    def dimension(self):#Imprimimos la matriz
        print("\n----Tablero---")
        for filatab in self.matriz:
            print(" [ " + "   " .join(filatab) + " ] ")
            

        
    

