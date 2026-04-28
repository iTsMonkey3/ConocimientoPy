
class Superheroe:
    
    def __init__(self,nombre,poder_principal):
        
        self.nombre = nombre
        self.poder_principal = poder_principal
        self.__energia = 100
        
    def usar_poder(self):
        if(self.__energia >= 20):
            print(f" ¡ {self.nombre} usa su {self.poder_principal} ! ")
            self.__energia -= 20
        else:
            print("Demasiado agotado, necesita descansar")
            
    def descansar(self):
        self.__energia = 100
    
    def moverse(self):
        print(f"{self.nombre} se está moviendo rápido")
        
    def ver_energia(self):
        return self.__energia
        
class Mutante(Superheroe):
    
    def __init__(self, nombre, poder_principal,nivel_mutante):
        
        super().__init__(nombre, poder_principal)
        self.nivel_mutante = nivel_mutante
        
    def evolucionar(self):
        self.nivel_mutante += 1
        print(f"¡{self.nombre} ha mutado al Nivel {self.nivel_mutante}!")
    
    def moverse(self):
        print(f"{self.nombre} corre dando saltos salvajes")
    
    def mutante_energia(self):
        self.__energia -= 50
        print(self.__energia)

class Mago(Superheroe):
    
    def __init__(self, nombre, poder_principal, varita):
        
        super().__init__(nombre, poder_principal)
        self.varita = varita
        
    def ataque_magico(self):
        print(f"{self.nombre} el mago ha usado su varita {self.varita}")
        
    def moverse(self):
        print(f"{self.nombre} se teletransporta usando magia")


super1 = Superheroe("Flash", "Rayo")
super2 = Superheroe("Arrow","Flecha")

super1.usar_poder()
print(super1.ver_energia())
# super1.usar_poder()
# super1.usar_poder()
# super1.usar_poder()
# super1.usar_poder()
# super1.usar_poder()

# super1.descansar()

# super2.usar_poder()
# super2.descansar()
        
wolverine = Mutante("Wolverie","Garras",20)
# wolverine.evolucionar()
# No deberia de mostrar nada por estar privada la energia
wolverine.mutante_energia()

# Wiwidiwa = Mago("Wiwidiwa","Fuego","Skibili")
# Wiwidiwa.ataque_magico()

# equipo = [super1,super2,wolverine,Wiwidiwa]

# for heroe in equipo:
#     heroe.moverse()
        