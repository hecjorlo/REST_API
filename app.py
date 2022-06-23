# Import libraries
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Flask setup
app = Flask(__name__)
# Connection to database: user=root, pasword="", port=3306
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/db_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Table creation
class User_Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

class User_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pc = db.Column(db.String(50))
    city = db.Column(db.String(50))

    def __init__(self, pc, city):
        self.pc = pc
        self.city = city

db.create_all()


# Main Page
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':"Welcome!"})

# Endpoint: POST a new User
@app.route('/users', methods=['POST']) 
def addUser():
    name = request.json['name']
    pc = request.json['pc']
    params = {'username':'hecjorlo', 'postalcode': pc}
    try:
        response = requests.get('http://api.geonames.org/postalCodeLookupJSON?', params=params).json()
        city = response['postalcodes'][0]['placeName']
    except Exception as ex:
        return jsonify({'message':'ERROR: Postal code not valid!'}), 404
    
    new_user_master = User_Master(name)
    new_user_details = User_Details(pc, city)   
    db.session.add(new_user_master)
    db.session.add(new_user_details)
    db.session.commit()
    return jsonify({'message':'User added Succesfully!', 
                    'user':name,
                    'pc':pc,
                    'city':city})

# Run app in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=4000)


