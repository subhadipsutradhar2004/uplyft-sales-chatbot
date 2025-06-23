from flask import Flask, request, jsonify
from flask_cors import CORS
from database import search_products

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("message", "")
    results = search_products(user_input)
    if results:
        response = "\n".join([f"{r['name']} - ₹{r['price']}" for r in results])
    else:
        response = "Sorry, no products found."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
