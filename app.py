from flask import Flask, jsonify

app  = Flask(__name__)

productos = [
    {"producto":"laptop","precio":800,"cantidad":4},
    {"producto":"mouse","precio":40,"cantidad":10},
    {"producto":"monitor","precio":500,"cantidad":2}
]

@app.route('/productos', methods=['GET'])
def datos():
    return jsonify({"productos":productos}) 

@app.route('/productos/<string:nombre>', methods=['GET'])
def getProduct(nombre):
    for salida in productos:
        if salida["producto"] == nombre:
            return jsonify({"producto":salida}) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)