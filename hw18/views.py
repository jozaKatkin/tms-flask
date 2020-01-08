from hw18.app import app, db
from flask import render_template, request, flash, redirect, url_for
from funcs import not_valid_product
from hw18.models import Product


@app.route("/")
def link():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("products.html", products=Product.query.all())


@app.route("/products/<int:product_id>", methods=["GET"])
def product_info(product_id):
    if request.method == "GET":
        product = Product.query.filter_by(id=product_id).first()
        if product:
            return render_template("product.html", product=product)
        flash(f"Product with {product_id} id does not exist", "danger")
        return redirect(url_for("products"))
    flash(f"This view supports only GET method", "danger")
    return redirect(url_for("products"))


@app.route("/products/<int:product_id>/delete", methods=["POST"])
def delete_button(product_id):
    if request.method == "POST":
        product = Product.query.filter_by(id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            flash("Product was successfully deleted!", "success")
            return redirect(url_for("products"))
        flash(f"Product with {product_id} id does not exist")
        return redirect(url_for("products"))
    flash(f"This view supports only GET method", "danger")
    return redirect(url_for("products"))


@app.route("/products/<int:product_id>/edit", methods=["POST", "GET"])
def edit_button(product_id):
    if request.method == "POST":
        try:
            if not_valid_product(request.form):
                flash("Enter all the fields", "warning")
            else:
                product = Product.query.filter_by(id=product_id).first()
                if product:
                    product.name = request.form["Name"]
                    product.price = request.form["Price"]
                    product.amount = request.form["Amount"]
                    product.comment = request.form["Comment"]
                    db.session.add(product)
                    db.session.commit()
                    flash("Product was successfully added", "success")
                    return redirect(url_for("products"))
            flash("Product with {product_id} id does not exist", "danger")
            return redirect(url_for("products.html"))
        except Exception:
            flash("Enter a valid data", "warning")
    elif request.method == "GET":
        product = Product.query.filter_by(id=product_id).first()
        if product:
            return render_template("edit_product.html", product=product)
        flash(f"Product with {product_id} id does not exist", "danger")
        return redirect(url_for("products"))
    flash(f"This view supports only GET and PUT methods", "danger")
    return redirect(url_for("products"))


@app.route("/products/add_product", methods=["POST", "GET"])
def add_button():
    if request.method == "POST":
        try:
            if not_valid_product(request.form):
                flash("Fields shouldn't be empty", "warning")
            else:
                product = Product(
                    name=request.form["Name"],
                    price=request.form["Price"],
                    amount=request.form["Amount"],
                    comment=request.form["Comment"],
                )
                db.session.add(product)
                db.session.commit()
                flash("Record was successfully added", "success")
                return redirect(url_for("products"))
        except Exception:
            flash("Enter a valid data", "warning")
    return render_template("add_product.html")
