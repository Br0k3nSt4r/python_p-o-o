class Coordenada:
    def __init__(self, x, y):
        self.__X= x
        self.__Y= y

    def getX(self):
        return self.__X
    def setX(self, x):
        self.__X= x

    def getY(self):
        return self.__Y
    def setY(self, Y):
        self.__Y= Y

    def mostrarCoordenada(self):
        print("(",self.__X,",",self.__Y,")")
