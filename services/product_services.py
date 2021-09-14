import requests
from flask import make_response, jsonify

from models.dbmodels import Product, ProductUser
from producer import publish


class ProductService:

    def get_all_products(self):
        return Product.query.all()

    def like(self, _id, db):
        req = requests.get('http://docker.for.mac.localhost:8000/api/user')
        json = req.json()

        try:
            product_user = ProductUser(user_id=json['id'], product_id=_id)
            db.session.add(product_user)
            db.session.commit()
            publish('product_liked', _id)
        except:
            return make_response(jsonify({'message': 'You already liked this product'}), 400)

        return jsonify({
            'message': f'Product {_id} liked'
        })
