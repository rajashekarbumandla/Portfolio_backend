"""Projects API routes."""
from flask import Blueprint, jsonify
from services.firebase_service import db
from utils.error_handlers import error_response, success_response

projects_bp = Blueprint("projects", __name__, url_prefix="/api")


@projects_bp.route("/projects", methods=["GET"])
def get_projects():
    """
    Fetch all projects from Firestore.

    Returns:
        JSON list of projects with id field
    """
    try:
        projects = []
        docs = db.collection("projects").stream()

        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            projects.append(data)

        return success_response(projects, "Projects fetched successfully")

    except Exception as e:
        return error_response(
            "Failed to fetch projects",
            status_code=500,
            error_details=str(e),
        )
