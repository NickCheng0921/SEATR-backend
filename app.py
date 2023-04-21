from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # Replace with your desired database URI
db = SQLAlchemy(app)
CORS(app)

debug=True

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)

    def __init__(self, code):
        self.code = code

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64))
    gradYear = db.Column(db.Integer)
    hobbies = db.Column(db.String(255))
    majInterest = db.Column(db.String(255))
    carInterest = db.Column(db.String(255))
    otherClass = db.Column(db.String(255))

# Create all tables and test
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/createcode/', methods=['POST'])
def create_code():
    if request.method == 'POST':
        # Get the string value from the request body
        request_data = request.get_json()
        code = request_data.get('code')
        print("Generating code ", code)


        # Create a new Code object and add it to the session
        new_code = Code(code=code)
        db.session.add(new_code)
        db.session.commit()

        if debug:
            codes = Code.query.all()  # Retrieve all code entries from the "Code" table
            code_returns = [code.code for code in codes]  # Return a list of code value
            return code
        else:
            return 'Code added successfully'
    else:
        return 'Invalid request'

@app.route('/createprofile', methods=['POST'])
def create_profile():
    # Get data from request

    code = request.form['code']
    grad_year = request.form['gradYear']
    hobbies = request.form['hobbies']
    maj_interest = request.form['majInterest']
    car_interest = request.form['carInterest']
    other_class = request.form['otherClass']

    # Create a new profile
    profile = Profile(code=code, gradYear=grad_year, hobbies=hobbies, majInterest=maj_interest, carInterest=car_interest, otherClass=other_class)
    db.session.add(profile)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'Profile created successfully'})


hostAddress = 'localhost'
if __name__ == '__main__':
    app.run(host=hostAddress, port=5000, debug=True)