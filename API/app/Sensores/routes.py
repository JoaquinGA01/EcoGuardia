from flask import Blueprint, request, jsonify
from app.models import Sensore 

sensores_blueprint = Blueprint('sensores', __name__)

@sensores_blueprint.route('/sensores', methods=['GET'])
def get_all_sensores():

    return

@sensores_blueprint.route('/sensores/<int:id>', methods=['GET'])
def get_sensor(id):

    return

@sensores_blueprint.route('/sensores', methods=['POST'])
def create_sensor():

    return

@sensores_blueprint.route('/sensores/<int:id>', methods=['PUT'])
def update_sensor(id):

    return

@sensores_blueprint.route('/sensores/<int:id>', methods=['DELETE'])
def delete_sensor(id):

    return


@sensores_blueprint.route('/sensores/Recomendacion', methods=['POST'])
def delete_sensor(Informacion):
    if (Informacion is not None):
        
        return
    else:
        return