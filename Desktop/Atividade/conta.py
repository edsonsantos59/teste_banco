import os
import time
import random
i = 1
j = 1
class Conta():    
    def __init__(self):  
        self.i = [] 
        self.nrConta = []      
        self.titular = []        
        self.saldo = []        
        self.limite = []   
    def info(self, i):     
        print("O número da conta é: " + str(self.nrConta[i])),
        print("Seu titular é: " + self.titular[i]),
        print("O saldo atual é: " + str(self.saldo[i])),
        print("E o limite atual é: " + str(self.limite[i]))  
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
        #if self.nrConta in aleatorio:
        #    print("Conta existente")
        #else:
        i = 1
        self.nrConta.append(i)
        self.titular.append(str(input("Qual o nome do titular da conta: ")))
        self.saldo.append(int(input("Deseja incluir quanto em dinheiro na conta: ")))
        self.limite.append(200)
        os.system('cls')
        print("Aguarde, estamos efetuando seu cadastro")
        time.sleep(5)
        os.system('cls')
        print("Sua conta foi criada!!!"),
        print("O número da conta é: " + str(self.nrConta)),
        print("Seu titular é: " + str(self.titular)),
        print("O saldo atual é: " + str(self.saldo)),
        print("E o limite atual é: " + str(self.limite))  
        i = i + 1
while(j < 1000):
    os.system("cls")
    conta = Conta()
    print("Sistema Bancário"),
    print("-------------------------------------")
    print("1 - Criar Conta"),
    print("2 - Realizar um Saque"),
    print("3 - Solicitar Informações de Conta")
    print("4 - Sair")
    opcao = int(input("Selecione uma das opções acima: "))
    if(opcao == 1):
        conta.criarConta()
    if(opcao == 2):
        conta.sacar()
    if(opcao == 3):
        conta.info(0)
    if(opcao == 4):
        exit
    j = j + 1