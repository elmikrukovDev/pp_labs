from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    app.run('localhost', '5000', debug = True)
