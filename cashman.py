import os 
from server import server
from db import db

environment = os.environ['FLASK_ENV']

if __name__ == '__main__':
    db.load()
    server.app.config['ENV'] = environment
    server.app.run(port=7000)
