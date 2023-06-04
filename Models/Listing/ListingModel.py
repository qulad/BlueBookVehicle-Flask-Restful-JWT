from datetime import datetime
from Models import db

class Listing(db.Model):
    listing_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    listing_active = db.Column(db.Boolean, nullable=False, default=False)
    new_waiting = db.Column(db.Boolean, nullable=False, default=True)
    new_vehicle_id = db.Column(db.Integer, nullable=True)
    edit_waiting = db.Column(db.Boolean, nullable=True, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    edited = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    