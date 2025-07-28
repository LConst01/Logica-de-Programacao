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