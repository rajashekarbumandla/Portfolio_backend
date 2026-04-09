"""Firebase initialization and database client."""
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def initialize_firebase():
    """
    Initialize Firebase Admin SDK using environment variable or .env file.

    Expects FIREBASE_KEY environment variable containing the Firebase
    credentials JSON as a string.

    Returns:
        Firestore client instance
    """
    try:
        # Get Firebase credentials from environment variable or .env file
        firebase_key_str = os.environ.get("FIREBASE_KEY")

        if not firebase_key_str:
            raise ValueError(
                "FIREBASE_KEY not found. Please:\n"
                "1. Create a .env file in backend folder\n"
                "2. Add: FIREBASE_KEY={your_firebase_json}\n"
                "Or set FIREBASE_KEY environment variable"
            )

        # Parse JSON string to dictionary
        cred_dict = json.loads(firebase_key_str)

        # Initialize Firebase with credentials
        cred = credentials.Certificate(cred_dict)

        # Only initialize if not already initialized
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)

        # Get Firestore client
        db = firestore.client()
        print("✅ Firebase initialized successfully")
        return db

    except json.JSONDecodeError as e:
        raise ValueError(f"FIREBASE_KEY is not valid JSON: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to initialize Firebase: {str(e)}")


# Initialize Firebase on module import
db = initialize_firebase()
