from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/calculate/<operation>', methods=['GET'])
def calculate(operation):
    try:
        # Extract query parameters
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            return jsonify({'error': 'Missing required query parameters: a and b'}), 400

        operations = {
            'add': lambda: add(a, b),
            'subtract': lambda: subtract(a, b),
            'multiply': lambda: multiply(a, b),
            'divide': lambda: divide(a, b)
        }

        if operation not in operations:
            return jsonify({'error': 'Invalid operation'}), 400

        result = operations[operation]()
        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
