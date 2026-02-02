from app import db

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "digipro"}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String)
    full_name = db.Column(db.String)

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("digipro.roles.id")
    )
    business_unit_id = db.Column(
        db.Integer,
        db.ForeignKey("digipro.business_units.id")
    )
    plant_id = db.Column(
        db.Integer,
        db.ForeignKey("digipro.plants.id")
    )

    is_active = db.Column(db.Boolean)
