from flask import Flask
from flask_cors import CORS
from controllers.product_controllers import ProductController, ProductLikeController
from models.dbmodels import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)
db.app = app
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/api/products')
def get():
    """
    Get all products
    :return: list of all products
    """
    return ProductController().get_all()


@app.route('/api/products/<int:_id>/like', methods=['POST'])
def post(_id):
    """
    give a like to a product
    :param _id: product id
    :return: confirmation message
    """
    return ProductLikeController().like(_id, db)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
