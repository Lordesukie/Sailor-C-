from flask import Flask, request, jsonify, render_template
import os

Weiss = Flask(__name__)

@Weiss.route('/celebrity', methods=['GET'])
def get_celebrity_info():
    name = request.args.get('name')
    celebrities = {
        "Jennie Kim": {"age": 28, "ethnicity": "Korean"},
        "Chris Evans": {"age": 43, "ethnicity": "Caucasian"},
    }
    info = celebrities.get(name, {"error": "Celebrity not found"})
    return jsonify({"name": name, "info": info})

@Weiss.route('/')
def home():
    return "Weiss.ai is working!"

if __name__ == '__main__':
    # Set to listen on the port provided by Render, default to 10000
    port = int(os.environ.get("PORT", 10000))
    Weiss.run(host='0.0.0.0', port=port)
