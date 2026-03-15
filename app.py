from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": ["Hello Student! 👋 How can I help you?", "Hi there! Need study help?"],
    "python": ["Python is a high-level programming language used in AI, ML and web development."],
    "dbms": ["DBMS stands for Database Management System. It stores and manages data."],
    "exam": ["Prepare daily, revise important topics, and practice previous question papers."],
    "assignment": ["Don't forget to submit your assignment before the deadline!"],
    "career": ["You can explore careers like AI Engineer, Web Developer, or Data Scientist."],
    "bye": ["Goodbye! Study well and have a great day!"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"].lower()

    for key in responses:
        if key in user_input:
            return jsonify(random.choice(responses[key]))

    return jsonify("Sorry, I didn't understand. Please ask something related to studies.")

if __name__ == "__main__":
    app.run(debug=True)