#Função x Classe 
#Função: Bloco de código que executa uma tarefa
#Classe: Modelo para cirar objetos
#Objeto:É uma estrutura que representa uma entidade do mundo real  ou conceito abstrato dentro deu um programa 

class ContaBancaria:
    def __init__(self, titular, saldo, saldo_inicial=0):
        #Quando utilizar __init__: quando precisa inicializar o objero com algum valor ou configuração
        self.titular = titular #instância atual do objeto
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor #self.saldo = self.valor
            print(f"Depósito de R${valor:.2f}") #:.2f serve para atribuir quantos números irão aparecer depois da virgula 
        else:
            print("Valor de depósito inválido!")
        #criar funções sacar e consultar_saldo
    def sacar(self, saque):
        if 0 < saque <= self.saldo:
            self.saldo -= saque
            print(f"Saque de R${saque:.2f}")
        else:
            print("Valor de saque inválido! Saldo insuficiente!")
            
    def consultar_saldo(self):
        print(f"Saldo atual; R${self.saldo:.2f}")

conta = ContaBancaria("Lucca", 1000000000)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()
