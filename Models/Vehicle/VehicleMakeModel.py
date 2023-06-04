from Models import db

class VehicleMake(db.Model):
    make_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    model_id = db.Column(db.Integer, nullable=False)
    make_year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    