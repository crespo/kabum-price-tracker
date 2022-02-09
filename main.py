import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ProductModel(db.Model):
    url = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    price = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f"Product:\nurl: {url}\ntitle: {title}\nprice: {price}"


db.create_all()  # comment if database is already created

resources_fields = {
    'url': fields.Integer,
    'title': fields.String,
    'price': fields.String
}


class Product(Resource):
    @marshal_with(resources_fields)
    def get(self, url):
        result = ProductModel.query.filter_by(url=url).first()
        if not result:
            abort(404, message='Could not find product with that URL...')
        return result

    @marshal_with(resources_fields)
    def put(self, url):
        result = ProductModel.query.filter_by(url=url).first()

        if result:
            abort(409, message='URL already registered...')

        product_info = new_product(url)
        title = product_info.get_title()
        price = product_info.get_price()

        product = ProductModel(url=url, title=title, price=price)
        db.session.add(product)
        db.session.commit()
        return product, 201


class ProductInfo:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price


def new_product(url):
    r = requests.get('https://www.kabum.com.br/produto/' + str(url)).text
    soup = BeautifulSoup(r, 'html.parser')
    title = soup.title.string
    price = soup.find(class_="regularPrice").string
    return ProductInfo(title, price)


api.add_resource(Product, '/product/<int:url>')

if __name__ == "__main__":
    app.run(debug=True)
