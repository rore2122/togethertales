from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main homepage."""
    # Assuming index.html is in the 'templates' folder
    return render_template('index.html')

@app.route('/cart')
def cart():
    """Renders the shopping cart page."""
    # This renders the detailed shopping cart HTML (cart.html)
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    """Renders the customer detail entry page."""
    # This renders the new checkout form (checkout.html)
    return render_template('checkout.html')

@app.route('/order_success')
def order_success():
    """Renders the order confirmation page with the unique code and WhatsApp link."""
    # This renders the success page with the 3-second timer logic (order_success.html)
    return render_template('order_success.html')

if __name__ == '__main__':
    # Run the application (accessible via http://127.0.0.1:5000/)
    app.run(debug=True)
