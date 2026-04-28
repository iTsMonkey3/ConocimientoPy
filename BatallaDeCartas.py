import random

class Superheroe:
    
    def __init__(self, nombre, hp_maximo, poder_principal):
        self.nombre = nombre
        self._hp = hp_maximo
        self.poder_principal = poder_principal
        
    def esta_vivo(self):
        if(self._hp <= 0):
            return False
        else:
            return True
    
    def recibir_dano(self, cantidad):
        self._hp -= cantidad
        if(self._hp <= 0):
            print(f"{self.nombre} está muerto")
        else:
            print(f"{self.nombre} ha sido atacado, le quedan {self._hp} puntos de vida")
    
    def atacar(self, objetivo):
        ataque = random.randint(10,20)
        print(f"{self.nombre} ha atacado a {objetivo.nombre} de forma epica")
        objetivo.recibir_dano(ataque)
        
        
    
class Mutante(Superheroe):
    
    def __init__(self, nombre, hp_maximo, poder_principal):
        super().__init__(nombre, hp_maximo, poder_principal)
        
    def atacar(self, objetivo):
        atina = random.randint(1,10)
        if (atina < 9):
            ataque = random.randint(20,35)
            print(f"{self.nombre} acertó el golpe critico de {ataque} a {objetivo.nombre}")
            objetivo.recibir_dano(ataque)
        else:
            print(f"{self.nombre} ha fallado su golpe")
            
class Mago(Superheroe):
    
    def __init__(self, nombre, hp_maximo, poder_principal):
        super().__init__(nombre, hp_maximo, poder_principal)
        
    def atacar(self, objetivo):
        print(f"{self.nombre} ha atacado a {objetivo.nombre} con {25} puntos de daño magico")
        objetivo.recibir_dano(25)
        
class JefeFinal:
    
    def __init__(self):
        self.nombre = "Bugzilla"
        self._hp = 200
        
    def esta_vivo(self):
        if(self._hp <= 0):
            return False
        else:
            return True
    
    def recibir_dano(self, cantidad):
        self._hp -= cantidad
        if(self._hp <= 0):
            print(f"{self.nombre} está muerto")
        else:
            print(f"{self.nombre} ha sido atacado, le quedan {self._hp} puntos de vida")
    
    def atacar_aleatorio(self, equipo):
        vivos = []
        for vivo in equipo:
            if (vivo.esta_vivo()):
                vivos.append(vivo)
        rival = random.choice(vivos)
        ataque = random.randint(15,30)
        print(f"{self.nombre} ha atacado a {rival.nombre} con un ataque de {ataque} de daño")
        rival.recibir_dano(ataque)
        
Super1 = Superheroe("Flash",100,"Rayo")
Muta1 = Mutante("Logan",150,"Arañar")
Mago1 = Mago("Harry",85,"fuego")

equipo = [Super1,Muta1,Mago1]

jefe = JefeFinal()

# Reemplaza tu 'while(jefe.esta_vivo ):' con esto:

while jefe.esta_vivo() and any(heroe.esta_vivo() for heroe in equipo):
    print("\n---  ¡NUEVA RONDA!  ---")
    
    # 1. Turno de los Héroes
    for heroe in equipo:
        # El héroe solo ataca si está vivo Y si el jefe sigue vivo
        if heroe.esta_vivo() and jefe.esta_vivo():
            heroe.atacar(jefe)
            
    # 2. Turno del Jefe
    # El jefe solo contraataca si sobrevivió a todos los golpes del equipo
    if jefe.esta_vivo():
        print("\n---  ¡TURNO DEL JEFE!  ---")
        jefe.atacar_aleatorio(equipo)

# 3. Conclusión de la batalla (fuera del while)
print("\n===  FIN DE LA BATALLA  ===")
if jefe.esta_vivo():
    print(" DERROTA... Bugzilla ha crasheado a todo tu equipo.")
else:
    print(" ¡VICTORIA! El equipo ha destruido a Bugzilla.")