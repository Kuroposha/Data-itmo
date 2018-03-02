from flask import Flask
from flask_pony import Pony

app = Flask(__name__)

import model
import views
