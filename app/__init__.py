from flask import Flask

App = Flask(__name__)
App.config.from_object('config')
from app import views
