from flask import Flask
from routes.correntista import correntista_route
from routes.contas import contas_route

app = Flask(__name__)

app.register_blueprint(correntista_route)
app.register_blueprint(contas_route)

app.run(debug=True)
