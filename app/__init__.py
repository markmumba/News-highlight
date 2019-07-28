from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap






 #initialize the application
app = Flask(__name__,instance_relative_config = True)

#Initializing flask Extension 
bootstrap = Bootstrap(app)

#setting up configurations 
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
from app import error