from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017')
db = client['NGO']


@app.route('/submit_donation', methods=['POST'])
def submit():
    try:
        data = request.json

        if 'uname' not in data or 'email' not in data or 'number' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        uname = data['uname']
        email = data['email']
        number = data['number']

        db.donation_form.insert_one({
            'username': uname,
            'email': email,
            'mobile_number': number
        })

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
