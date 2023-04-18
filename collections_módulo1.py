class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Código: {} Saldo: {} <<]".format(self.codigo, self.saldo)


conta_hugo = ContaCorrente(2505)
print(conta_hugo)

conta_geovana = ContaCorrente(6543)
conta_geovana.deposita(1000)
print(conta_geovana)

contas = [conta_geovana, conta_hugo]

for conta in contas:
    print(conta)
