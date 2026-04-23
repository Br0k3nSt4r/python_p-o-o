# Prog. Orien. a Obj.
Introduccion a la Programacion Orientada a Objetos en Python

## Porque aprender P.O.O?

- Imagina que quieres crear tu propio Juego, tienes Guerreros, Magos, Dragones.. etc, cada uno consus propias habilidades, PV, y ataques. ¿Como los organizas en codigo SIN repetir todo una y otra y otra y otr..?

- La **Programacion Orientada a 0bjetos** es la respuesta. En lugar de escribir instrucciones sueltas, modelas el Mundo Real con *objetos* que tienen Caracteristicas y Comportamientos. Siendo la forma baase en la que muchos *Programas Profesionales* estan hechos

![POO](img/poo.png "POO")

## Clase y Objeto

- Una CLASE es un tipo de dato cuyas variables se llaman -OBJETOS o -instancias

- La CLASE es la definicion del concepto* del Mundo Real y los -OBJETOS o -instancias son el propio "OBJETO" del Mundo Real

- Las CLASES estan compuestos por dos elementos:
    - **Atributos:** Informacion que  ALMACENA la clase
    - **Metodos:** Operaciones que pueden REALIZARSEN con la clase

## Definicion de una CLASE en Python

```py
class NombreClase:

    def __init__(self, variable1, variable2):
        self.atributo1= valor1
        self.atributo2= valor2

    def NombreMetodo(self):
        BloqueCodigo
```

- `class`: Palabra reservada en Python para definir una CLASE
- `NombreClase`: Nombre de la CLASE que se quiere crear
- `def`: Palabra reservada en Pyton para definir tanto al Constructor de la CLASE (metodo que se ejecuta al usar una CLASE por primera vez) como a los diferentes metodos que tiene
- `__init__`: Plabra reeservada en Python para definir el Metodo Constructor de la CLASE, le metodo __inif__ es una de las cosas que primero se ejecutan al crear una CLASE
- `(self, variableX)`: Parametro del Constructor de la CLASE, El parametro **self** es OBLIGATORIO para despues poder tener tantos parametros como quierass :D, y la forma de añadir parametros es la misma que en las funciones
- `(self, atributoX)`: Forma de utilizacion y acceso a los atributos de la CLASE
- `NombreAtributo`: Nombre del metodo de la CLASE
- `self`:Parametro del Constructor de la CLASE, El parametro **self** es OBLIGATORIO para despues poder tener tantos parametros como quierass :D, y la forma de añadir parametros es la misma que en las funciones
- `BloqueCodigo`: Instrucciones que ejecuta el metodo

**Al definir una CLASE, !Ten en cuenta!**
- Puedes definir TANTOS atrubutos como necesites :3
- Pwedes definir TANTOS metodos como necesites :3
- Puedes definir TANTOS parametros en el Constructor y en los metodos como necesites -w-"
