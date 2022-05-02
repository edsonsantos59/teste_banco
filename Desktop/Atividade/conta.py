import os
import time
import random
aleatorio = []
class Conta():    
    def __init__(self):    
        self.id = 0    
        self.nrConta = 9999999999        
        self.titular = "--"        
        self.saldo = 0        
        self.limite = 200   
    def info(self, id):     
        if (self.id == id):     
            print("O número da conta é: " + str(self.nrConta)),
            print("Seu titular é: " + self.titular),
            print("O saldo atual é: " + str(self.saldo)),
            print("E o limite atual é: " + str(self.limite))  
    def depositar(self, valorDepositar):        
        self.valorDepositar = valorDepositar        
        self.saldo = self.valor + self.saldo        
        return self.saldo       
    def extrato(self):        
        return self.saldo    
    def sacar(self, valorSacar):        
        self.saldo = self.saldo - self.valorSacar        
        if self.saldo > -100:            
            print("Operação cancelada, você não possui saldo suficiente")            
            return        
        elif self.saldo < 0:            
            print("Transação efetuada com sucesso. Você está utilizando R$" + self.saldo + " do seu limite")        
        else:            
            print("Transação efetuada com sucesso") 
    def criarConta(self):
        self.nrConta = random.randint(0,2)
        if self.nrConta in aleatorio:
            print("Conta existente")
        else:
            aleatorio.append(self.nrConta)
            self.titular = str(input("Qual o nome do titular da conta: "))
            self.saldo = int(input("Deseja incluir quanto em dinheiro na conta: "))
            os.system('cls')
            print("Aguarde, estamos efetuando seu cadastro")
            time.sleep(5)
            os.system('cls')
            print("Sua conta foi criada!!!"),
            print("O número da conta é: " + str(self.nrConta)),
            print("Seu titular é: " + str(self.titular)),
            print("O saldo atual é: " + str(self.saldo)),
            print("E o limite atual é: " + str(self.limite))  
            print(aleatorio)
conta = Conta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()
conta.criarConta()