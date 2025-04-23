from flask import Flask, request, jsonify
from calculator import (add, subtract, multiply, divide)

app = Flask(__name__)

@app.route('/calculate/<operation>', methods=['POST'])
def calculate(operation):
    try:
        data = request.get_json()
        operations = {
            'add': lambda: add(data['a'], data['b']),
            'subtract': lambda: subtract(data['a'], data['b']),
            'multiply': lambda: multiply(data['a'], data['b']),
            'divide': lambda: divide(data['a'], data['b'])
        }
        
        if operation not in operations:
            return jsonify({'error': 'Invalid operation'}), 400
            
        result = operations[operation]()
        return jsonify({'result': result})
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except KeyError:
        return jsonify({'error': 'Missing required parameters'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)