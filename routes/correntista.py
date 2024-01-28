from flask import Blueprint, request
from database.database import correntistas
from utils.estrutura_base import Correntista

correntista_route = Blueprint('correntista', __name__)


@correntista_route.route('/correntista')
def listar_correntistas():
    lista_clientes = []
    for cliente in correntistas:
        user = {
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "endereco": cliente.endereco,
            "profissao": cliente.profissao,
        }
        lista_clientes.append(user)

    return lista_clientes


@correntista_route.route('/correntista', methods=['POST'])
def cadastrar_correntistas():
    body = request.json

    new_correntista = Correntista(
        body['nome'], body['cpf'], body['endereco'], body['profissao'])

    correntistas.append(new_correntista)

    return {"mensagem": "Correntista cadastrado com sucesso",
            "data": {
                "nome": new_correntista.nome,
                "cpf": new_correntista.cpf,
                "endereco": new_correntista.endereco,
                "profissao": new_correntista.profissao,
            }}
