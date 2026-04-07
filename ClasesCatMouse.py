from   Tablero import   Tablero
class Animal:
    def __init__(self,fila, columna, tablero):#este es el construcctor como en java, se ejecuta una sola vez
        self.fila= fila
        self.columna= columna
        self.tablero=tablero
    
    def mover(self, new_fila, new_columna):
        if self.tablero.es_posicion_valida(nueva_fila, nueva_columna):
            self.fila = nueva_fila
            self.columna = nueva_columna
            print(f"Movido a {self.fila}, {self.columna}")
        else:
            print("No puedes salir del tablero.")

    def atrapa(self,animal2):#En este metodo estamos realizando la condicion de que el gato atrape al raton
        if self.fila == animal2 and self.columna == animal2:#Si el gato esta en la ubicacion
            print("El gato atrapo al ratón")
            return True#Devolvemos verdadero
        else:
            print("El ratón escapó")
            return False#Sino devolvemos false
            
    def __str__(self):
        # Esto te ayudará a imprimir la posición fácilmente
        return f"Posición: ({self.fila}, {self.columna})"

    


class Cat(Animal):

    pass

class Mouse(Animal):
    pass