from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/calculate/<operation>', methods=['GET', 'POST'])
def calculate(operation):
    try:
        # Handle both GET and POST requests
        if request.method == 'GET':
            a = request.args.get('a', type=float)
            b = request.args.get('b', type=float)
        else:  # POST
            data = request.get_json()
            a = float(data['a'])
            b = float(data['b'])

        if a is None or b is None:
            return jsonify({'error': 'Missing required parameters: a and b'}), 400

        operations = {
            'add': lambda: add(a, b),
            'subtract': lambda: subtract(a, b),
            'multiply': lambda: multiply(a, b),
            'divide': lambda: divide(a, b)
        }

        if operation not in operations:
            return jsonify({'error': f'Invalid operation. Valid operations: {list(operations.keys())}'}), 400

        result = operations[operation]()
        return jsonify({
            'operation': operation,
            'result': result,
            'a': a,
            'b': b
        })

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except KeyError:
        return jsonify({'error': 'Missing required parameters in JSON body'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
