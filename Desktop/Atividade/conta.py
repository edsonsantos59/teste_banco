import os
import time
i = 1
class Conta():    
    def __init__(self):  
        self.finalizar = ""
        self.i = [] 
        self.nrConta = []      
        self.titular = []        
        self.saldo = []        
        self.limite = []   
    def info(self):  
        self.conta = int(input("Digite o número da conta que deseja verificar as informações: "))
        for i in self.nrConta:
            print("O número da conta é: " + self.nrConta(i)),
            print("Seu titular é: " + self.titular(i)),
            print("O saldo atual é: " + self.saldo(i)),
            print("E o limite atual é: " + self.limite(i))
        self.finalizar = input("Pressione Enter para continuar!") 
    def depositar(self):
        nrConta = int(input("Digite o número da conta: "))
        if(nrConta <= i or nrConta <= 0):     
            valorDepositar = int(input("Digite um valor para depositar em sua conta: "))
            if(valorDepositar > 0 or valorDepositar < 1000):   
                self.valorDepositar = valorDepositar        
                self.saldo = self.valorDepositar + int(self.saldo[nrConta])      
                print("O valor atual de sua conta é R$ " + str(self.saldo)) 
                self.finalizar = input("Pressione qualquer tecla para continuar! ")
            else:
                print("Valor não pode ser menor ou igual a 0 ou maior ou igual a 1000! "),
                self.finalizar = input("Pressione qualquer tecla para continuar! ")  
        else:
            print("Número da conta inexistente! "),
            self.finalizar = input("Pressione qualquer tecla para continuar! ")
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
    def criarConta(self, i):
        #if self.nrConta in aleatorio:
        #    print("Conta existente")
        #else:
        self.nrConta.append(i)
        self.titular.append(str(input("Qual o nome do titular da conta: ")))
        self.saldo.append(int(input("Deseja incluir quanto em dinheiro na conta: ")))
        self.limite.append(200)
        os.system('cls')
        print("Aguarde, estamos efetuando seu cadastro")
        time.sleep(5)
        os.system('cls')
        print("Sua conta foi criada!!!"),
        i = i + 1