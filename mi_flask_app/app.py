from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from route import *

with app.app_context():     
    # Inicializamos la DB     
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)