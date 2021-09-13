import requests
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    __table_args__ = (db.UniqueConstraint('user_id', 'product_id'),)


@app.route('/api/products')
def get_all():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:_id>/like', methods=['POST'])
def like(_id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    json = req.json()

    try:
        product_user = ProductUser(user_id=json['id'], product_id=_id)

        db.session.add(product_user)
        db.session.commit()
        publish('product_liked', _id)
    except:
        return make_response(jsonify({'message':'You already liked this product'}), 400)

    return jsonify({
        'message': f'Product {_id} liked'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
