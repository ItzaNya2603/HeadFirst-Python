class Gato:
    def __init__(self, nombre: str, raza: str) -> None:
        self.nombre = nombre
        self.raza = raza
        self.hambre = True
        self.energia = 100 #Empieza con la energia al cien, nuevo estado
        self.animo = "tranquila" #Humor de akimi inicial
#Se definen las caracteristicas o estado inicial de kiminella


    def comer(self) -> None:
        self.hambre = False
        self.energia += 10
        print(f"{self.nombre} ha comido churu y recupero energia.")

    def jugar(self) -> None:
        if self.energia > 20:
            self.energia -= 30 #Cuando akimi juega, pierde energia
            self.hambre = True #Jugar tambien le dara hambre
            self.animo = "Muy feliz!"
            print(f"{self.nombre} esta persiguiendo un juguete. Se divierte mucho!")
        else:
            print(f"{self.nombre} esta muy cansada para jugar ahora.")    

    def __repr__(self) -> str:
        estado_hambre = "tiene hambre" if self.hambre else "está llena"
        return f"Gatita: {self.nombre} ({self.raza}) | Energia: {self.energia}% | Animo: {self.animo} y {estado_hambre}."