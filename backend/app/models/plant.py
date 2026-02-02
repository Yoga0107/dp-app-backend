from app import db

class Plant(db.Model):
    __tablename__ = "plants"
    __table_args__ = {"schema": "digipro"}

    id = db.Column(db.Integer, primary_key=True)
    business_unit_id = db.Column(
        db.Integer,
        db.ForeignKey("digipro.business_units.id")
    )
    name = db.Column(db.String(100))
    code = db.Column(db.String(50))
    location = db.Column(db.String(100))
