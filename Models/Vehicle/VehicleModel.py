from flask import url_for
from datetime import datetime
from Models import db, default_image_url

class Vehicle(db.Model):
    vehicle_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    vehicle_image_url = db.Column(db.String(200), nullable=False, default=default_image_url)
    type_id = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, nullable=False)
    model_id = db.Column(db.Integer, nullable=False)
    make_id = db.Column(db.Integer, nullable=False)
    fuel_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    engine_type_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    thousand_km = db.Column(db.Integer, nullable=False)
    tork = db.Column(db.Float, nullable=True)
    battery_capacity = db.Column(db.Float, nullable=True)
    range_km = db.Column(db.Integer, nullable=True)
    charge_time = db.Column(db.Float, nullable=True)
    charge_watt = db.Column(db.Float, nullable=True)
    shift_id = db.Column(db.Integer, nullable=False)
    used = db.Column(db.Boolean, nullable=False)
    drive_id = db.Column(db.Integer, nullable=False)
    door_count = db.Column(db.Integer, nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)
    body_id = db.Column(db.Integer, nullable=False)
    engine_volume = db.Column(db.Float, nullable=True)
    parking_sensor = db.Column(db.Boolean, nullable=False)
    glass_rooftop = db.Column(db.Boolean, nullable=False)
    central_console = db.Column(db.Boolean, nullable=False)
    folding_mirror = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def get_vehicle_image_url(self):
        vehicle_image_url = url_for("static", self.vehicle_image_url)
        return vehicle_image_url

    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    