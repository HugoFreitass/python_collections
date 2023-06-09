from abc import ABCMeta, abstractmethod
from functools import total_ordering

class Conta(metaclass = ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>> Código: {} Saldo: {} <<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
         self._codigo = codigo
         self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[Código {}, Saldo {}]".format(self._codigo, self._saldo)


conta_hugo = ContaCorrente(2505)
print(conta_hugo)

conta_geovana = ContaPoupanca(6543)
conta_geovana.deposita(1000)
print(conta_geovana)

contas = [conta_geovana, conta_hugo]

for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)


conta_funcionario1 = ContaSalario(5000)
conta_funcionario2 = ContaSalario(1223)
conta_funcionario3 = ContaSalario(2450)

conta_funcionario1.deposita(2000)
conta_funcionario2.deposita(1250)
conta_funcionario3.deposita(3000)

contas_salario = [conta_funcionario1, conta_funcionario2, conta_funcionario3]

for conta in sorted(contas_salario):
    print(conta) #as contas serão impressas em ordem crescente de saldo
