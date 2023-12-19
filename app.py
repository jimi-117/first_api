from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "products": [
        {"id": 1, "name": "Orange", "price": 500},
        {"id": 2, "name": "Redbull", "price": 100},
        {"id": 3, "name": "Monster", "price": 200},
        {"id": 4, "name": "Nuka coke", "price": 300}
    ]
}

@app.route("/", methods=["GET"])
def get_data():
    return jsonify(data["products"])


# Api to get product
@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    for product in data["products"]:
        if product["id"] == product_id:
            return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

@app.route("/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    data["products"].append(new_product)
    return jsonify(new_product), 201



if __name__ == '__main__':
    app.run(debug=True)