from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Dummy cart to store items
cart = []

@app.route('/')
def favicon():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def show_cart():
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form.get('item')
    price = float(request.form.get('price'))
    cart.append({'item': item, 'price': price})
    return redirect(url_for('index'))

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    cart.clear()  # Clear the cart
    return redirect(url_for('show_cart'))  # Redirect back to the cart page

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
