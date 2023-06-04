from Models import db

class VehicleDrive(db.Model):
    drive_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    drive_type = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    