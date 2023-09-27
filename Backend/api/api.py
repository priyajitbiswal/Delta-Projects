from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize a counter
counter = 0

@app.route('/index', methods=['GET'])
def hello_world():
    global counter
    counter += 1

    # Return response in JSON format
    response = {
        "response": "Hello World!",
        "times-requested": counter
    }

    return jsonify(response)

@app.route('/translate', methods=['POST'])
def translate_text():
    # Get JSON data from the request
    data = request.get_json()

    # You can implement translation here based on the provided data
    # Ensure you return the translation in JSON format

    # For demonstration, let's assume translation happens here
    translated_text = f"Translated: {data['text']} to {data['dest_lang']}"

    response = {
        "translation": translated_text
    }

    return jsonify(response)

@app.route('/detect', methods=['POST'])
def detect_language():
    # Get JSON data from the request
    data = request.get_json()

    # You can implement language detection here based on the provided data
    # Ensure you return the detected language in JSON format

    # For demonstration, let's assume language detection happens here
    detected_language = "English"

    response = {
        "detected-language": detected_language
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
