from flask import Flask, Response, request
from flask_cors import CORS

from math import pow

app = Flask(__name__)
#Esta línea lo que hace es que yo pueda acceder a mi api desde direcciones ip externas
# o desde otros programas porque por defecto las aplicaciones bloquean este tipo de conexiones.
cors = CORS(app, resources = {r"/*": {"origin":"*"}}) 

@app.route('/')
def index():
    return 'Hola mundo, que tal'


@app.route('/datos', methods=['GET'])
def get_datos():
    save_file = open('save_file.txt', 'r+')
    return Response(status=200,
                    response=save_file.read(),
                    content_type='text/plain')


@app.route('/datos', methods=['POST'])
def post_data():
    str_file = request.data.decode('utf-8')
    save_file = open('save_file.txt', 'w+')
    save_file.write(str_file)
    save_file.close()
    return Response(status=204)


@app.route('/potencia', methods=['GET'])
def potencia():
    num_1 = int(request.args.get('num_1'))
    num_2 = int(request.args.get('num_2'))

    return str(int(pow(num_1, num_2)))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)