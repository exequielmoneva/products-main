from services.product_services import ProductService
from flask_restful import Resource


class ProductController(Resource):
    def __init__(self):
        self.product_service = ProductService()

    def get_all(self):
        return self.product_service.get_all_products()


class ProductLikeController(Resource):
    def __init__(self):
        self.product_service = ProductService()

    def like(self, _id, db):
        return self.product_service.like(_id, db)
