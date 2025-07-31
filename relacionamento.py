#Crie um sistema simples para registrar e exibir relacionamentos amorosos entre pessoas
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.parceiros = []
    
    def adicionar_parceiro(self, relacionamento):
        self.parceiros.append(relacionamento)
    
    def mostrar_parceiros(self):
        if not self.parceiros:
            print(f"{self.nome} não possui parceiros registrados.")
        else:
            print(f"Parceiros amorosos de {self.nome}")
            for rel in self.parceiros:
                if rel.pessoa1 == self:
                    parceiro = rel.pessoa2
                else:
                    parceiro = rel.pessoa1
                print(f"- {parceiro.nome}, desde {rel.ano_inicio}")

class Relacionamento:
    def __init__(self, pessoa1, pessoa2, ano_inicio): #self: relacionamento ao objeto que está sendo criado/manipulado
        self.pessoa1 = pessoa1 
        self.pessoa2 = pessoa2
        self.ano_inicio = ano_inicio
        
    def mostrar_informacao(self):
        print(f"{self.pessoa1.nome} e {self.pessoa2.nome} estão juntas desde {self.ano_inicio}")
        
#criando pessoas

ana = Pessoa("Ana")
bruno = Pessoa("Bruno")
ronaldo = Pessoa("Ronaldo")
davi_brito = Pessoa("Davi Brito")
judite = Pessoa("Judite")
raquel = Pessoa("Raquel")


#Criando relacionamento
relacionamento1 = Relacionamento(ana, davi_brito, 2015)
relacionamento2 = Relacionamento(bruno, raquel, 2022)
relacionamento3 = Relacionamento(ronaldo, judite, 2010)

#adicionar realcioanmentos às Pessoas 
ana.adicionar_parceiro(relacionamento1)
davi_brito.adicionar_parceiro(relacionamento1)

bruno.adicionar_parceiro(relacionamento2)
raquel.adicionar_parceiro(relacionamento2)

ronaldo.adicionar_parceiro(relacionamento3)
judite.adicionar_parceiro(relacionamento3)

#exibir
ana.mostrar_parceiros()
davi_brito.mostrar_parceiros()
bruno.mostrar_parceiros()
raquel.mostrar_parceiros()
ronaldo.mostrar_parceiros()
judite.mostrar_parceiros()