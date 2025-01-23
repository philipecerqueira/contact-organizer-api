from flask import Blueprint, Response, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/", methods=["GET"])
def health_check() -> Response:
    """Verifica se a API está funcionando"""
    return jsonify({"message": "A API está funcionando!"}), 200
