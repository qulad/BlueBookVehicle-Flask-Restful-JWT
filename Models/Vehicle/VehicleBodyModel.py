from Models import db

class VehicleBody(db.Model):
    body_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    body_type = db.Column(db.String(100), nullable = False)
    
    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    