from flask import jsonify, make_response

def response_ok(message, data=None):
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    return make_response(jsonify(response), 200)

def response_created(message, data=None):
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    return make_response(jsonify(response), 201)

def response_bad_request(message):
    response = {
        'status': 'error',
        'message': message
    }
    return make_response(jsonify(response), 400)

def response_unauthorized(message):
    response = {
        'status': 'error',
        'message': message
    }
    return make_response(jsonify(response), 401)

def response_not_found(message):
    response = {
        'status': 'error',
        'message': message
    }
    return make_response(jsonify(response), 404)

def response_internal_server_error(message):
    response = {
        'status': 'error',
        'message': message
    }
    return make_response(jsonify(response), 500)

