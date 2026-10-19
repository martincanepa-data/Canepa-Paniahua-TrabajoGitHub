import numpy as np 

class Matriz():
    def __init__(self, datos):
        self.matriz = np.array(datos)
        self.filas, self.columnas = self.matriz.shape
    
    def es_cuadrada(self):
        return self.filas == self.columnas
    
    def __str__(self):
        return f'Matriz de {self.filas} x {self.columnas}: \n {self.matriz}'


    # Sobrecarga de operadores

    def __add__(self, otra):
        if self.matriz.shape != otra.matriz.shape:
            raise Exception("Las matrices tienen que ser de la misma dimension para poder sumarse")
        return Matriz(self.matriz + otra.matriz)

    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Matriz(self.matriz * escalar)
        raise Exception("La multiplicacion con '*' solo esta permitida con escalares")

    def __rmul__(self, otro):
        return self.__mul__(otro)

    def __matmul__(self, otra):
        if self.columnas != otra.filas:
            raise Exception("Las matrices no son aptas para multiplicarse entre sí")
        return Matriz(self.matriz @ otra.matriz)
    def __sub__(self, otra):
        if self.matriz.shape != otra.matriz.shape:
            raise Exception("Las matrices tienen que ser de la misma dimension para poder restarse")
        return Matriz(self.matriz - otra.matriz)


matriz = Matriz([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
matriz2 = Matriz([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matriz + matriz2)
print(matriz - matriz2)
print(matriz @ matriz2)
print(matriz * 3)
print(3 * matriz)
print(matriz.es_cuadrada())