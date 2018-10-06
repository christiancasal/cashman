from mongoengine import connect

def load():
    connect('mlbdata', port=27017)