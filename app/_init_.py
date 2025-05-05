from flask import Flask

app = Flask(_name_)
from app import views

if _name_=='_main_':
    app.run()