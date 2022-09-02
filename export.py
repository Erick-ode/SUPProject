import os
from flask import Blueprint, jsonify, send_from_directory
from flask_login import login_required, current_user
from autentication.login import is_admin

export = Blueprint('export', __name__)

directory = '.\\files\\csv_files'


@export.route('/arquivos', methods=['GET'])
def list_files():
    files = []

    for file_name in os.listdir(directory):
        path_address = os.path.join(directory, file_name)
        if os.path.isfile(path_address):
            files.append(file_name)

    return jsonify(files)


@export.route('/arquivos/<file_name>', methods=['GET'])
def get_file(file_name):
    return send_from_directory(directory, file_name, as_attachment=True)
