from flask import Blueprint, request
from database.database import correntistas

contas_route = Blueprint('contas', __name__)
numero_conta = 1


@contas_route.route('/conta/<cpf_cliente>/corrente', methods=['POST'])
def cadastro_conta_corrente(cpf_cliente):
    data = request.json
    global numero_conta
    user = None
    for cliente in correntistas:
        if cliente.cpf == cpf_cliente:
            user = cliente

    if (user == None):
        return {"Mensagem": "Correntista não encontrado"}

    conta_corrente = user.cadastrar_conta_corrente(
        numero_conta, data['agencia'])

    numero_conta += 1

    return {
        "mensagem": "Conta corrente criada",
        "info_conta": {
            "numero_conta": conta_corrente.numero_conta,
            "agencia": conta_corrente.agencia,
            "tipo_conta": conta_corrente.tipo_conta
        }
    }


@contas_route.route('/conta/<cpf_cliente>/poupanca', methods=['POST'])
def cadastro_conta_poupanca(cpf_cliente):
    data = request.json
    global numero_conta
    user = None

    for cliente in correntistas:
        if cliente.cpf == cpf_cliente:
            user = cliente

    if (user == None):
        return {"Mensagem": "Correntista não encontrado"}

    conta_poupanca = user.cadastrar_conta_poupanca(
        numero_conta, data['agencia'])

    numero_conta += 1

    return {
        "mensagem": "Conta poupança criada",
        "info_conta": {
            "numero_conta": conta_poupanca.numero_conta,
            "agencia": conta_poupanca.agencia,
            "tipo_conta": conta_poupanca.tipo_conta
        }
    }


@contas_route.route('/contas/<int:numero_conta>/saldo')
def consultar_saldo(numero_conta):
    for cliente in correntistas:
        for conta in cliente.contas:
            if conta.numero_conta == numero_conta:
                info_conta = conta

    return {"numero_conta": info_conta.numero_conta,
            "agencia": info_conta.agencia,
            "tipo_conta": info_conta.tipo_conta,
            "saldo": info_conta.saldo}


@contas_route.route('/contas/<int:numero_conta>/depositar', methods=['POST'])
def depositar(numero_conta):
    data = request.json

    for cliente in correntistas:
        for conta in cliente.contas:
            if conta.numero_conta == numero_conta:
                info_conta = conta

    info_conta.depositar(data['valor'])

    return {"Mensagem": "Depósito realizado com sucesso"}


@contas_route.route('/contas/<int:numero_conta>/sacar', methods=['POST'])
def sacar(numero_conta):
    data = request.json

    for cliente in correntistas:
        for conta in cliente.contas:
            if conta.numero_conta == numero_conta:
                info_conta = conta

    resposta = info_conta.sacar(data['valor'])

    return {"Mensagem": resposta}


@contas_route.route('/contas/<int:numero_conta>/juros', methods=['POST'])
def calcular_juros(numero_conta):
    data = request.json

    for cliente in correntistas:
        for conta in cliente.contas:
            if conta.numero_conta == numero_conta:
                info_conta = conta

    resposta = info_conta.calcular_juros(data['taxa_juros'])

    return {"Mensagem": resposta}
