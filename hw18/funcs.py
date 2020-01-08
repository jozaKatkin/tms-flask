def not_valid_product(form):
    return not form["Name"] or not form["Price"] or not form["Amount"]
