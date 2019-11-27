#

from flask import Flask
from flask_redis import FlaskRedis

App = Flask(__name__)
App.config.from_object('config')

if 'REDIS_URL' in App.config:
    redis_client = FlaskRedis(App)
    try:
        redis_client.ping()
    except:
        redis_client = None

from app import views
