from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import StoreScheme
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError
from flask import abort
from db import db

blp = Blueprint("Stores", "stores", description="Operations on stores")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreScheme(many=True))
    def get(self):
        stores = StoreModel.query.all()
        return stores

    @blp.arguments(StoreScheme)
    @blp.response(201, StoreScheme)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while creating store")
        return store


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreScheme)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store