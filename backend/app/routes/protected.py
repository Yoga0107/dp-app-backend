from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.permissions import role_required
from app.constants.roles import ADMIN, OFFICER, USER

protected_bp = Blueprint("protected", __name__)


@protected_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    claims = get_jwt()
    return jsonify({
        "user": claims
    })


@protected_bp.route("/admin-only", methods=["GET"])
@role_required(ADMIN)
def admin_only():
    return jsonify({"message": "Welcome Admin"})


@protected_bp.route("/officer-dashboard", methods=["GET"])
@role_required(ADMIN, OFFICER)
def officer_dashboard():
    return jsonify({"message": "Officer Dashboard"})


@protected_bp.route("/user-dashboard", methods=["GET"])
@role_required(ADMIN, OFFICER, USER)
def user_dashboard():
    return jsonify({"message": "User Dashboard"})
