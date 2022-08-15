from random import randint

class ContaBanco:
   
   def __init__(self, nome, telefone, renda_mensal, conta, saldo, cheque_especial, sexo):  
     self.nome = nome
     self.telefone = telefone
     self.renda = renda_mensal
     self._conta = randint(1, 9999) #número aleatório
     self._saldo = int(saldo)
     self._cheque_especial= False
     self._sexo = sexo #0=masculino 1 feminino

   def ChequeEspecial(self,sexo):
      if (self._sexo == 1) : 
         self._cheque_especial= True

   def deposito(self,deposito):
      self._saldo += deposito
      return f'Deposito de R${deposito} . Saldo atual da conta é de R${self._saldo}'
   
   def saque(self,valor_saque):
      valor_max_saque = self.renda + self._saldo #calcular saque max conta cheque especial
      if ((self._cheque_especial == True) and (valor_saque <= valor_max_saque )):
         self._saldo -= valor_saque
         return f'Saque de R${valor_saque}. Saldo atual da conta é de R${self._saldo}'

      elif ((self._cheque_especial == False) and (valor_saque <= self._saldo)):
         self._saldo -= valor_saque
         return f'Saque de R${valor_saque}. Saldo atual da conta é de R${self._saldo}'
      else:
         if(self._cheque_especial == True):
               return f'Saldo insuficiente para realizar o saque de {valor_saque}. O valor disponível para saque é de {valor_max_saque}'
         else:
               return f'Saldo insuficiente para realizar o saque de {valor_saque}. O valor disponível para saque é de {self._saldo}'

class Cliente(ContaBanco):
   
   def __init__(self, nome, telefone, renda_mensal, conta, saldo, cheque_especial, sexo, is_titular):  
     super().__init__(nome, telefone, renda_mensal, conta, saldo, cheque_especial, sexo)
     self._is_titular= True
   
   def consultaDoBanco(self, nome, telefone, renda_mensal):
      return f'Nome: {self.nome}, Telefone: {self.telefone}, Renda mensal: R${self.renda}'

 
cliente1 = Cliente('Andre', '1234-5678', 2000, '', '2000','',0,'')
cliente2 = Cliente('Andreia', '8765-4321', 1000, '', '2000','',1,'')

conta1 = cliente1
conta2 = cliente2

cliente3 = Cliente('Bruno', '2234-5678', 3000, '', '3000','',0,'')

print('----Exemplo cliente homem-----')
print(cliente1.consultaDoBanco(cliente1.nome, cliente1.telefone,cliente1.renda))
conta1.ChequeEspecial(conta1)
print(f'Saldo atual de {conta1.nome} é de {conta1._saldo}')
print(conta1.deposito(1000))
print(conta1.deposito(1000))
print(conta1.saque(1000))
print(conta1.saque(1000))
print(conta1.saque(1000))
print(conta1.saque(2000))
print('---Exemplo cliente mulher------')
print(cliente2.consultaDoBanco(cliente2.nome, cliente2.telefone,cliente2.renda))
conta2.ChequeEspecial(conta2)
print(f'Saldo atual de {conta2.nome} é de {conta2._saldo}')
print(conta2.saque(2050))
print(conta2.saque(1050))
