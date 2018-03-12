from flask import Flask
from flask_pony import Pony
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('settings.BaseConfig')

pony = Pony(app)
CSRFProtect(app)
Bootstrap(app)

import model
import views

pony.connect()
