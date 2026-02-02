from app import db

class BusinessUnit(db.Model):
    __tablename__ = "business_units"
    __table_args__ = {"schema": "digipro"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(50))
