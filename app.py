from flask import Flask, request, jsonify
from chatbot import Chatbot
from analytics import Analytics
from student_model import Student
from educator_model import Educator
from content_model import Content

app = Flask(__name__)

chatbot = Chatbot()
analytics = Analytics()

@app.route('/student', methods=['POST'])
def handle_student_interaction():
    student_data = request.get_json()
    student = Student(student_data)
    response = chatbot.respond(student)
    analytics.track_student_interaction(student, response)
    return jsonify(response)

@app.route('/educator', methods=['POST'])
def handle_educator_interaction():
    educator_data = request.get_json()
    educator = Educator(educator_data)
    response = analytics.get_educator_insights(educator)
    return jsonify(response)

@app.route('/content', methods=['POST'])
def handle_content_interaction():
    content_data = request.get_json()
    content = Content(content_data)
    response = chatbot.respond(content)
    analytics.track_content_interaction(content, response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
