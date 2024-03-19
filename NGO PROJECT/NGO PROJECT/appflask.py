from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient()  # Connect to the default MongoDB instance on localhost:27017
db = client['NGO']
donation_collection = db['donation_form']
contact_collection = db['Contact_form']

@app.route("/")
def mainpage():
    return render_template("mainpage.html")

@app.route("/Aboutus")
def Aboutus():
    return render_template("Aboutus.html")

@app.route("/DONATEPAGE")
def DONATEPAGE():
    return render_template("DONATEPAGE.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/appcode")
def appcode():
    return render_template("appcode.html")

@app.route("/sravanthicode")
def sravanthicode():
    return render_template("sravanthicode.html")

@app.route("/kavyaqrcode")
def kavyaqrcode():
    return render_template("kavyaqrcode.html")

@app.route("/niyazqrcode")
def niyazqrcode():
    return render_template("niyazqrcode.html")

@app.route('/submit_donation', methods=['POST'])
def submit_donation():
    try:
        data = request.json

        if 'uname' not in data or 'email' not in data or 'number' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        uname = data['uname']
        email = data['email']
        number = data['number']

        donation_collection.insert_one({
            'username': uname,
            'email': email,
            'mobile_number': number
        })

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error in submit_donation:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.json

        if 'fname' not in data or 'lname' not in data or 'subject' not in data or 'interested' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        fname = data['fname']
        lname = data['lname']
        subject = data['subject']
        interested = data['interested']

        contact_collection.insert_one({
            'fname': fname,
            'lname': lname,
            'subject': subject,
            'interested': interested
        })

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error in submit_contact:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
