from flask import Blueprint, Response

from app import app

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/camila')
def index():
    """ Documentación"""
    return b"<h1> Camila Guerrero</h1>"
    # return Response("Camila", status=200)
    # return "Hola Pygroup! {}".format(name)
