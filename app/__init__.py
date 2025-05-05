from flask import Flask

app = Flask(__name__)
from app import views

if __name__=='_main_':
    app.run()