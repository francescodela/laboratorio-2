class Mascota  :
    def __init__ (self , edad, color, tipo ):
        self.edad = edad 
        self.color = color 
        self.tipo = tipo 
matias = Mascota (5, "blanco", "perro")
zara = Mascota (2, "naranja", "gato" )
 
print (type (matias))
print (type (zara))

print (matias.__dict__)
print (zara.__dict__)

