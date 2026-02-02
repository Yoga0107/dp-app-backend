from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.models.role import Role
from app.utils.security import hash_password, check_password, generate_token, create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        print("PAYLOAD:", data)

        email = data.get("email")
        if not email.endswith("@cpp.co.id"):
            return jsonify({"message": "Only @cpp.co.id allowed"}), 400

        role = Role.query.filter_by(name="user").first()
        print("ROLE:", role)

        user = User(
            email=email,
            full_name=data.get("full_name"),
            password_hash=hash_password(data.get("password")),
            role_id=role.id,
            is_active=True
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Signup success"}), 201

    except Exception as e:
        print("SIGNUP ERROR:", e)
        return jsonify({"error": str(e)}), 500



@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Email and password required"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password(data["password"], user.password_hash):
        return jsonify({"message": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"message": "User inactive"}), 403

    # ✅ JWT PAYLOAD YANG BENAR
    access_token = create_access_token(
        identity=str(user.id),  # sub
        additional_claims={
            "email": user.email,
            "role_id": user.role_id,
            "plant_id": user.plant_id,
            "business_unit_id": user.business_unit_id
        }
    )

    return jsonify({
        "access_token": access_token,
        "token_type": "Bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "role_id": user.role_id,
            "plant_id": user.plant_id,
            "business_unit_id": user.business_unit_id
        }
    }), 200

@auth_bp.route("/ping", methods=["GET"])
def ping():
    return {"message": "auth alive"}