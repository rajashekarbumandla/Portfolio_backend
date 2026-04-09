"""Health check route."""
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return jsonify(
        {
            "success": True,
            "message": "Backend Running Successfully 🚀",
            "status": "online",
        }
    )


@health_bp.route("/health", methods=["GET"])
def health():
    """Detailed health check endpoint."""
    return jsonify(
        {
            "success": True,
            "status": "healthy",
            "message": "Server is running",
        }
    )
