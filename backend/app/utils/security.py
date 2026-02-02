import bcrypt
from flask_jwt_extended import create_access_token

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def generate_token(user):
    return create_access_token(
        identity=user.id,
        additional_claims={
            "role_id": user.role_id,
            "plant_id": user.plant_id,
            "business_unit_id": user.business_unit_id
        }
    )
