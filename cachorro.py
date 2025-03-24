class Cachorro:
    def _init_(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 100
        self.comida = comida
        self.acordado = False
        self.feliz = False
 
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} Está acordado!")
    def dormir(self):
        self.acordado = False
        self.energia = 100
        print(f"{self.nome} Está dormindo!")
    def brincar(self):
        if self.acordado:
            if self.energia >= 20:
                self.energia -= 20
                self.feliz = True               
                print(f"{self.nome} Está brincando e está feliz!")
            else:
                print(f"{self.nome} Não tem energia para brincar!")
        else:
            print(f"{self.nome} Está dormindo, não pode brincar!")
    def ignorar(self):
        self.feliz = True
        print(f"{self.nome} Está triste!")
    def comer(self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome} Está comendo!")
        else:
            print(f"{self.nome} Está dormindo, não pode comer!")
    def latir(self):
        if self.acordado:
            print(f"{self.nome} Está latindo!")
        else:
            print(f"{self.nome} Está dormindo, não pode latir")



    
    def exibirStatus(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Comida: {self.comida} unidades")
        print(f"Acordado: {self.acordado}")
        print(f"Feliz: {self.feliz}")
        print(f"Energia: {self.energia} unidades")

cachorro1 = Cachorro("Nali", 3, "Golden Retriever",8)
cachorro1.exibirStatus()
cachorro1.brincar()
cachorro1.acordar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.dormir()
cachorro1.acordar()
cachorro1.brincar()