class Animal:
    def __init__(self,fila, columna):#este es el construcctor como en java, se ejecuta una sola vez
        self.fila= fila
        self.columna= columna
    
    def mover(self, new_fila, new_columna):
        self.fila = new_fila
        self.columna = new_columna

class cat(Animal):
    pass

class mouse(Animal):
    pass