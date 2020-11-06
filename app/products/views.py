from http import HTTPStatus
from flask import Blueprint, Response, request

from app.products.models import get_all_categories, create_new_category

products = Blueprint("products", __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {
    "message": "",
    "data": [],
    "errors": [],
    "metadata": []
}


@products.route('/dummy-product', methods=['GET', 'POST'])
def dummy_product():
    """ This method test the request types. If is GET Type it will
    render the text Products in h1 label with code 500.
    If is POST Type it will return Empty shelve! with status code 403
    """
    if request.method == 'POST':
        return EMPTY_SHELVE_TEXT, HTTPStatus.FORBIDDEN

    return PRODUCTS_TITLE, HTTPStatus.INTERNAL_SERVER_ERROR


@products.route('/dummy-product-2')
def dummy_product_two():
    """ This method shows how Response object could be used to make API
    methods.
    """
    return Response(DUMMY_TEXT, status=HTTPStatus.OK)


@products.route('/categories')
def get_categories():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    categories = get_all_categories()

    RESPONSE_BODY["message"] = "OK"
    RESPONSE_BODY["data"] = categories

    return RESPONSE_BODY, 200


@products.route('/add-category', methods=['POST'])
def create_category():
    """

    :return:
    """
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])

        return Response("Category created!", status=201)
