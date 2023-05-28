from flask import Flask, render_template, abort
from flask import send_file
import os
app = Flask(__name__)

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):

    BASE_DIR = 'C:/Users/margo/OneDrive/Documentos/Ingeniería en Computación/Sexto semestre/Seminario de Traductores II/Proyecto final/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Archivos'
    abs_path = os.path.join(BASE_DIR, req_path)
    if os.path.isfile(abs_path):
        return send_file(abs_path)
    if not os.path.exists(abs_path):
        return abort(404)
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
