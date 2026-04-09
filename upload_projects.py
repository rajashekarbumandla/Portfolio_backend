import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------------------
# YOUR PROJECTS DATA
# -----------------------------
projects = [

    {
        "title": "AHybrid Graph Learning And Reconstruction-Based Framework For Credit Card Fraud Detection",
        "description": "Advanced fraud detection system leveraging Graph Neural Networks and Autoencoders to identify suspicious transactions",
        "points": [
            "Modeled financial transactions as graph structures using GraphSAGE",
            "Implemented autoencoders to learn normal transaction behavior and detect anomalies",
            "Analyzed user-transaction relationships to identify fraud patterns",
            "Improved detection accuracy by combining graph-based learning with anomaly detection"
        ],
        "tech": ["Python", "PyTorch", "PyTorch Geometric", "GraphSAGE", "Autoencoders"],
        "image": "https://images.unsplash.com/photo-1556745757-8d76bdb6984b",
        "github": "https://github.com/b-rahul07/Fraud-Gaurd",
        "demo": "https://fraud-gaurd-mu.vercel.app/"
    },

    {
        "title": "Employee Salary Prediction System",
        "description": "Machine learning-based system to predict employee salaries using real-world survey data",
        "points": [
            "Built regression models using Random Forest and XGBoost for accurate predictions",
            "Performed data cleaning, preprocessing, and feature engineering",
            "Evaluated models using performance metrics to improve accuracy",
            "Deployed the model as an interactive web app using Streamlit"
        ],
        "tech": ["Python", "Scikit-learn", "Pandas", "XGBoost", "Streamlit"],
        "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f",
        "github": "https://github.com/rajashekarbumandla/Employee-Salary-prediction",
        "demo": ""
    },

    {
        "title": "Similar Image Finder using Deep Learning",
        "description": "Computer vision system that finds visually similar images using deep learning techniques",
        "points": [
            "Used Convolutional Neural Networks (CNN) for feature extraction",
            "Applied K-Nearest Neighbors (KNN) for similarity matching",
            "Built an interactive interface using Streamlit for image upload",
            "Enabled real-time image comparison for recommendation systems"
        ],
        "tech": ["Python", "CNN", "KNN", "OpenCV", "Streamlit"],
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475",
        "github": "https://github.com/your-link",
        "demo": ""
    }

]

internships = [

    {
        "role": "Python Developer Intern",
        "company": "Infosys Springboard",
        "duration": "Oct 2024 – Dec 2024",
        "points": [
            "Led a team of 4 members to develop a real-time Weather and Air Quality Monitoring system",
            "Built backend logic using Python and Flask with API integration",
            "Processed and visualized real-time environmental data",
            "Improved application performance through testing, debugging, and optimization"
        ],
        "tech": ["Python", "Flask", "REST APIs", "Data Visualization"]
    },

    {
        "role": "Artificial Intelligence Intern",
        "company": "IBM SkillsBuild",
        "duration": "May 2025 – Jul 2025",
        "points": [
            "Developed an Employee Salary Prediction system using machine learning models",
            "Applied Random Forest and XGBoost for regression tasks",
            "Performed data preprocessing, feature engineering, and model evaluation",
            "Deployed the solution using Streamlit for interactive usage"
        ],
        "tech": ["Python", "Scikit-learn", "Pandas", "XGBoost", "Streamlit"]
    },

    {
        "role": "Artificial Intelligence Intern",
        "company": "UptoSkills",
        "duration": "Jan 2026 – Present",
        "points": [
            "Gaining hands-on experience in machine learning and web development",
            "Implemented core AI/ML concepts through guided projects",
            "Worked on data handling, preprocessing, and model building",
            "Collaborated with mentors to understand real-world problem solving"
        ],
        "tech": ["Python", "Machine Learning", "HTML", "CSS"]
    }

]

# -----------------------------
# UPLOAD TO FIREBASE
# -----------------------------
for project in projects:
    db.collection("projects").add(project)

print("All projects uploaded successfully!")

for intern in internships:
    db.collection("internships").add(intern)

print("Internships uploaded successfully!")