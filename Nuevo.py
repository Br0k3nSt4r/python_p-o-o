class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad

    def mostrarPersona(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellido)
        print("Edad: ", self.edad)
"""
def main():
    print("Vamos a  aprender P.O.O en Python.../")
    persona1= Persona("Lorenzo", "Perez", 18)
    persona1.mostrarPersona()


if __name__ == "__main__":
    main()
"""