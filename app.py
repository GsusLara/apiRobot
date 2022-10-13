import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename 

app  = Flask(__name__)

@app.route('/', methods=['POST'])
def upload():
    file     = request.files['archivo']
    basepath = os.path.dirname (__file__) 
    upload_path = os.path.join (basepath, 'static/archivos', secure_filename(file.filename)) 
    file.save(upload_path)
    return jsonify({"messaje":"imagen cargada"}),200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)