from Nuevo import Persona

Juan= Persona("Juan", "Castellanos", 15)
Juan.mostrarPersona()

Leidy= Persona("Leidy", "Alvarez", 18)
Leidy.mostrarPersona()

Leidy.apellido= "Perez"
Leidy.mostrarPersona()

Juan= Leidy
Juan.mostrarPersona()