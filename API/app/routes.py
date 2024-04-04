from flask import Blueprint, request, jsonify
import json
from app.utils import *

main = Blueprint('main', __name__)


@main.route('/',methods=['GET'])
def saludo():
    return jsonify({"Respuesta": "Bienvenido a EcoGuardian"})









# Informacion Usuarios