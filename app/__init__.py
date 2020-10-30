from flask import Flask


app = Flask(__name__)


from app.products import views
from app.products.views import products
app.register_blueprint(products)

if __name__ == "__main__":
    app.run(debug=True)