from flask import render_template, request, redirect
from pony.orm import db_session
from flask_pony.views import CreateView, UpdateView

from app import app
from forms import CustomerForm
from model import Customer
from repositories import CategoryRepository

@app.route('/registration', methods=['GET', 'POST'])
@db_session
def customer_create():
    form = CustomerForm(request.form)

    if form.validate_on_submit():
        customer = Customer(phone=form.phone.data,
                            email=form.email.data,
                            name=form.name.data)
        return redirect('/')

    return render_template('customer/create.html', form=form)

class CategoryCreate(CreateView):
    decorators = [db_session]
    repository_class = CategoryRepository
    sucсess_endpoint = 'category_update'

class CategoryUpdate(UpdateView):
    decorators = [db_session]
    repository_class = CategoryRepository
    sucсess_endpoint = 'category_update'

app.add_url_rule('/category/add', view_func=CategoryCreate.as_view('category_create'))
app.add_url_rule('/category/edit/<id>', view_func=CategoryUpdate.as_view('category_update'))
