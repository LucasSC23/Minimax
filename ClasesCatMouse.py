class Animal:
    def __init__(self,fila, columna):#este es el construcctor como en java, se ejecuta una sola vez
        self.fila= fila
        self.columna= columna
    
    def mover(self, new_fila, new_columna):
        self.new_fila = new_fila
        self.new_columna = new_columna

    def atrapa(self,animal2):#En este metodo estamos realizando la condicion de que el gato atrape al raton
        if self.fila == animal2 and self.columna == animal2:#Si el gato esta en la ubicacion
            return True#Devolvemos verdadero
        else:
            return False#Sino devolvemos false

    


class cat(Animal):

    pass

class mouse(Animal):
    pass