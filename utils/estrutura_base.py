class Correntista:
    def __init__(self, nome, cpf, endereco, profissao):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.profissao = profissao
        self.contas = []

    def cadastrar_conta_corrente(self, numero_conta, agencia, saldo_inicial=0.0):
        nova_conta = ContaCorrente(numero_conta, agencia, saldo_inicial)
        self.contas.append(nova_conta)
        return nova_conta

    def cadastrar_conta_poupanca(self, numero_conta, agencia, saldo_inicial=0.0):
        nova_conta = ContaPoupanca(numero_conta, agencia, saldo_inicial)
        self.contas.append(nova_conta)
        return nova_conta


class ContaCorrente:
    def __init__(self, numero_conta, agencia, saldo_inicial=0.0, limite=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.limite = limite
        self.agencia = agencia
        self.tipo_conta = "Corrente"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return "Saque realizado com sucesso"
        else:
            return "Saque não realizado"

    def calcular_juros(self, taxa_juros):
        if self.saldo < 0:
            juros = self.saldo * taxa_juros
            self.saldo += juros
            return f"O seu saldo após calcular o juros é {self.saldo}"
        else:
            return "Seu saldo não se encontra negativo"


class ContaPoupanca:
    def __init__(self, numero_conta, agencia, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.agencia = agencia
        self.tipo_conta = "Poupança"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return "Saque realizado com sucesso"
        else:
            return "Saque não realizado"

    def calcular_juros(self, taxa_juros):
        juros = self.saldo * taxa_juros
        self.saldo += juros
        return f"O seu saldo após calcular o juros é {self.saldo}"
