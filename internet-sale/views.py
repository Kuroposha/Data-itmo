from flask import render_template
from app import app

@app.route('/registration')
def customer_create():
    return render_template('customer/create.html')
