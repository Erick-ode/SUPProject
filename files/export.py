from os import path, listdir
from flask import Blueprint, jsonify, send_from_directory
from flask_login import login_required
from files.generate import pd, divide_dataframes, create_csv

export = Blueprint('export', __name__)

directory = './files/csv_files'


@export.route('/arquivos', methods=['GET'])
@login_required
def list_files():
    files = []

    for file_name in listdir(directory):
        path_address = path.join(directory, file_name)
        if path.isfile(path_address):
            files.append(file_name)

    return jsonify(files)


@export.route('/arquivos/<file_name>/<ag_id>', methods=['GET'])
@login_required
def get_file(file_name, ag_id):
    create_csv('./files/csv_files/creation.csv', './sup.sql', ag_id)
    df_all = pd.read_csv(f'{directory}/creation.csv', sep=',', encoding='windows-1252')

    df_total = divide_dataframes(df_all)

    df_managers = df_all['Nome'].unique()
    dfs = []
    for name in df_managers:
        df_person = df_all.loc[df_all['Nome'] == name]
        df_register = divide_dataframes(df_person, name)
        dfs.append(df_register)

    with pd.ExcelWriter(f'{directory}/{file_name}') as writer:
        df_total.to_excel(writer, sheet_name='Total', index=False)
        for df in dfs:
            df.to_excel(writer, sheet_name=f'{df["Nome"].loc[~df["Nome"].isna()].item()}', index=False)

    return send_from_directory(directory, file_name, as_attachment=True)
