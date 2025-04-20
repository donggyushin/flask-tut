from db import db

class ItemTagModel(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Interger, primary_key=True)
    item_id = db.Column(db.Interger, db.ForeignKey("items.id"))
    store_id = db.Column(db.Interger, db.ForeignKey("stores.id"))