from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/timbrooks/instruct-pix2pix"
API_TOKEN = "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"  # Replace with your valid token

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

@app.route('/translate', methods=['POST'])
def translate():
    image_file = request.files['image']
    image_bytes = image_file.read()

    response = requests.post(API_URL, headers=headers, files={"file": image_bytes})
    result = response.json()

    if isinstance(result, dict) and result.get("error"):
        return jsonify({"error": result["error"]})

    return jsonify({"url": result[0]["image"] if "image" in result[0] else "No image returned"})

if __name__ == '__main__':
    app.run(debug=True)
