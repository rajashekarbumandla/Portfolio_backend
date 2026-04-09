"""
Portfolio Backend - Flask API Server

This is the main application file for the portfolio backend.
It initializes Flask with proper configuration and registers all routes.

Environment Variables Required:
  - FIREBASE_KEY: Firebase credentials as JSON string
"""
import os
from flask import Flask
from flask_cors import CORS

# Import route blueprints
from routes.health import health_bp
from routes.projects import projects_bp
from routes.internships import internships_bp


def create_app():
    """
    Application factory function.

    Creates and configures the Flask app with all blueprints and middleware.

    Returns:
        Flask app instance
    """
    app = Flask(__name__)

    # Configure Flask
    app.config["JSON_SORT_KEYS"] = False

    # Enable CORS for all routes
    CORS(app)

    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(internships_bp)

    # Global error handler for 404
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Route not found", "success": False}, 404

    # Global error handler for 500
    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error", "success": False}, 500

    return app


# Create app instance
app = create_app()


if __name__ == "__main__":
    # Get environment variables
    debug_mode = os.environ.get("DEBUG", "False").lower() == "true"
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))

    # Run the app
    print(f"\n🚀 Starting Portfolio Backend Server...")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   Debug: {debug_mode}\n")

    app.run(
        host=host,
        port=port,
        debug=debug_mode,
    )
