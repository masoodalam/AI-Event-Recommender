from flask import Flask, request, jsonify
from recommender import recommend_events

app = Flask(__name__)

@app.route('/')
def home():
    return 'AI Event Recommender is running!'

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    if not user_data:
        return jsonify({"error": "Invalid input"}), 400
    recommendations = recommend_events(user_data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
