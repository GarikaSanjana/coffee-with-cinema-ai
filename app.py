from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Coffee With Cinema Backend Running"

@app.route("/generate_script", methods=["POST"])
def generate_script():

    data = request.json

    title = data.get("title")
    genre = data.get("genre")
    idea = data.get("idea")
    characters = data.get("characters")

    scenes = [
        "Scene 1: Introduction of characters",
        "Scene 2: Story conflict begins",
        "Scene 3: Major twist in the plot",
        "Scene 4: Final climax"
    ]

    dialogues = [
        "Character: Something strange is happening.",
        "Character: We must solve this mystery.",
        "Character: This changes everything."
    ]

    result = {
        "title": title,
        "genre": genre,
        "idea": idea,
        "characters": characters,
        "scenes": scenes,
        "dialogues": dialogues
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)