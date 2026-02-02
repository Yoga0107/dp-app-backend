from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import jsonify
from functools import wraps
from app.models.user import User


def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id, is_active=True).first()
    return user
