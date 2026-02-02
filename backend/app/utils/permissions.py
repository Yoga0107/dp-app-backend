from flask_jwt_extended import jwt_required, get_jwt
from functools import wraps
from flask import jsonify


def role_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            role_id = claims.get("role_id")

            from app.models.role import Role
            role = Role.query.filter_by(id=role_id).first()

            if not role or role.name not in allowed_roles:
                return jsonify({
                    "message": "Forbidden",
                    "required_roles": allowed_roles
                }), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
