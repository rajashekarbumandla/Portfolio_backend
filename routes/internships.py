"""Internships API routes."""
from flask import Blueprint, jsonify
from services.firebase_service import db
from utils.error_handlers import error_response, success_response

internships_bp = Blueprint("internships", __name__, url_prefix="/api")


@internships_bp.route("/internships", methods=["GET"])
def get_internships():
    """
    Fetch all internships from Firestore.

    Returns:
        JSON list of internships with id field
    """
    try:
        internships = []
        docs = db.collection("internships").stream()

        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            internships.append(data)

        return success_response(internships, "Internships fetched successfully")

    except Exception as e:
        return error_response(
            "Failed to fetch internships",
            status_code=500,
            error_details=str(e),
        )
