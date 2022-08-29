## to set up flask we write this command

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


##This top few commands can be copied as they are available in the documentation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

 ##In db we are passing flask app. Calling db variable because we need to make the connection between the flask
db = SQLAlchemy(app) 

##Creating the class 
##db.model will inherit the value for Drink 

class Drink(db.Model):
    
    ## we will create the columns 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100))

    ##__repr__ method for the representation. When I use drink objct to print then representation self method comes in as it prints
    ## .name and .description

    def __repr__(self):

        ##self will refer to the objects 
        # f will be used to paramterized the strings
        return f"{self.name} - {self.description} - {self.id}"


##creating an endpoint by providing the path
##when someone hits "/" then it should follow the route


@app.route('/')
def index():
    return("Hello")

## we will change the path to drinks 
 

@app.route('/drinks')
def get_drinks():

    ##we need to route the data stored in the class Drink and it should go in /drinks
    ##Data stored like Cherry, oranges, etc.
    drinks = Drink.query.all()

    ## we cannot simply just put drinks over there. in order to do that we need to iterate and put it in the empty strings
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description, 'id' : drink.id}
        output.append(drink_data)
    return {'drinks': output}

##Adding the route for ID
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, "description": drink.description}


##Adding the another route for drinks and using the method post to write new data

##For this postman will come into handy as it will be very easy for us to post the new data
@app.route('/drinks', methods = ['POST'])
def add_drink():
    drink = Drink(name = request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()

    ##drink.id will get added into the drink variable in our function 
    return {'id':drink.id}

##If we want to delete a particular drink then write 

@app.route('/drinks/<id>', methods = ['DELETE'])

##taking ID as the parameter over here 
## we will be using the postman again to check that field has been deleted or not

def delete_drink(id):
    drink = Drink.query.get(id)
    db.session.delete(drink)
    db.session.commit()

    return {"message": "Hooray"}