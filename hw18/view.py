from hw18.app import app, db
from flask import render_template, request
from hw18.models import Product


@app.route("/")
def link():
    return render_template("index.html")


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@app.route("/products/<id>")
def product_info(id):
    product = Product.query.filter(Product.id == id).first()
    return render_template("product.html", product=product)


@app.route("/products/<id>")
def delete_button(id):
    product = Product.query.filter(Product.id == id).first()
    db.session.delete(product)
    db.session.commit()
    return "Saved"


@app.route("/products/<id>", methods=["POST"])
def edit_button(id):
    if request.method == 'POST':
        product = Product.query.filter(Product.id == id).first()
        value_name = request.form["Value to edit"]
        new_value = request.form["New value"]
        setattr(product, value_name, new_value)
        db.session.add(product)
        db.session.commit()
    return "Saved"


@app.route("/products", methods=["POST"])
def add_button():
    if request.method == 'POST':
        name = request.form["Name"]
        price = request.form["Price"]
        amount = request.form["Amount"]
        comment = request.form["Comment"]
        product = Product(name=name, price=price, amount=amount, comment=comment)
        db.session.add(product)
        db.session.commit()
    return products()
