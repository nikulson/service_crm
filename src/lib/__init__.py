from flask_sqlalchemy import SQLAlchemy

from src import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\PROJECTS\\service_crm\\service.db'
db = SQLAlchemy(app)
