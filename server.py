# Done individually

from flask import Flask, request, jsonify
from main import process1, process2

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.
@app.route('/process1', methods=['POST'])
def execute_process1():
    
    data = request.get_data()
    processed = process1(data)
    res = jsonify({'list': processed})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/process2', methods=['POST'])
def execute_process2():
    
    data = request.get_data()
    processed = process2(data)
    res = jsonify({'list': processed})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')