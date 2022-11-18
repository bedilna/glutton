# glutton
Commands to use because you're on Windows Powershell: 

To activate virtural environment: ./venv/Scripts/activate 

After installing dependencies, run: pip3 freeze > requirements.txt

$env:FLASK_APP="application.py"
$env:FLASK_ENV="development"
python -m flask run 



As of Flask-SQLAlchemy 3.0, all access to db.engine (and db.session) requires an active Flask application context. db.create_all uses db.engine, so it requires an app context.

with app.app_context():
    db.create_all()
When Flask handles requests or runs CLI commands, a context is automatically pushed. You only need to push one manually outside of those situations, such as while setting up the app.

Instead of calling create_all in your code, you can also call it manually in the shell. Use flask shell to start a Python shell that already has an app context and the db object imported.

$ flask shell
>>> db.create_all()
Or push a context manually if using a plain python shell.

$ python
>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all()

Adding a drink to the database 
from application import Drink 
drink=Drink(name="Grape Soda", description="Tastes like grapes")

db.session.add(drink) 
db.session.commit() 
Drink.query.all() 

Another way to add a drink: 
db.session.add(Drink(name="Cherry juice", description="Tastes like that one ice cream"))
db.session.commit() 

