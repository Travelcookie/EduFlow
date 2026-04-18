from flask import Flask, jsonify

app = Flask(__name__)

COURSES = [
    {"id": 1, "title": "DevOps Grundlagen", "students": 1240},
    {"id": 2, "title": "Python für Data Science", "students": 890},
    {"id": 3, "title": "Web Security", "students": 567},
]

@app.route("/")
def home():
    return jsonify({"app": "EduFlow", "version": "1.0", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/courses")
def courses():
    return jsonify({"courses": COURSES, "count": len(COURSES)})

@app.route("/courses/<int:course_id>")
def course_detail(course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course is None:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)