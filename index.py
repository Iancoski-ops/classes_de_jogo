class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "Mago":
            ataque = "Magia"
        elif self.tipo == "Guerreiro":
            ataque = "Espada"
        elif self.tipo == "Monge":
            ataque = "Artes marciais"
        else:
            ataque = "Shuriken"

        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = Heroi("Gabriel", "23", "Monge")
heroi1.atacar()

heroi2 = Heroi("Yuri", "30", "Ninja")
heroi2.atacar()

heroi3 = Heroi("Prisley", "26", "Guerreiro")
heroi3.atacar()

heroi4 = Heroi("Lainner", "34", "Mago")
heroi4.atacar()