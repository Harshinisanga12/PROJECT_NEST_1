from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['NGO']

@app.route('/submit_contact', methods=['POST'])
def submit():
    try:
        data = request.json

        if 'fname' not in data or 'lname' not in data or 'subject' not in data or 'interested' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        fname = data['fname']
        lname = data['lname']
        subject = data['subject']
        interested = data['interested']

        db.Contact_form.insert_one({
            'firstname': fname,
            'lastname': lname,
            'subject': subject,
            'interested': interested
        })

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
