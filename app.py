from flask import Flask, jsonify, render_template
app = Flask(__name__)

products = [
    {"id": 1, "name": "iPhone 15", "price": 999},
    {"id": 2, "name": "Samsung S24", "price": 899},
    {"id": 3, "name": "Xiaomi 14", "price": 699}
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({
        "success" : True,
        "data": products,
        "message": "Get all products successfully!"
    })
@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)

    if product:
        return jsonify({"success": True, "data": product, "message": "Get product successfully!"})
    else:
        return jsonify({"success": False, "message": "Product not found"}), 404
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)