from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Flask setup
app = Flask(__name__)

# SQLAlchemy setup (make a connection to the database code)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Store data as models: 
class Drink(db.Model):   # type: ignore
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=True, nullable=False)
    description= db.Column(db.String(120))
    
    def __repr__(self): 
        return f"{self.name} - {self.description}"
    

@app.route('/')
def index(): 
        return 'Hello!'
    
    
@app.route('/drinks')
def get_drinks(): 
    drinks = Drink.query.all()
    
    output = []
    for drink in drinks: 
        drink_data = {'name': drink.name, 'description': drink.description}
        
        output.append(drink_data)
    
    return {"Drinks": output} 

@app.route('/drinks/<id>')
def get_drink(id): 
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description} 

@app.route('/drinks', methods=['POST'])
def add_drink(): 
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}
    
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id): 
    drink = Drink.query.get_or_404(id)
    # if drink is None: 
    #     return {"error": "drink not found1"}
    db.session.delete(drink)
    db.session.commit() 
    return {"message": "drink has been deleted"}
    
    
    
@app.route('/food')
def get_foods(): 
    return {"Fooood": "food data is here!"} 
