from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Age classification API'

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    if 'age' not in data:
        return jsonify({
            'error': 'age is required' 
        }), 400

    if not isinstance(data['age'], int):
        return jsonify({
            'error': 'age must be integer'
        }), 400

    age = data['age']

    if age < 0 or age > 100:
        return jsonify({
            'error': 'age must be between 0 and 100'
        }), 400

    if age < 18:
        result = 'child'
    elif age < 60:
        result = 'adult'
    else:
        result = 'senior'

    return jsonify({
        'You Are': result
    }), 200

if __name__ == '__main__':
    app.run(debug=True)