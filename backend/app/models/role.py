from app import db

class Role(db.Model):
    __tablename__ = "roles"
    __table_args__ = {"schema": "digipro"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
