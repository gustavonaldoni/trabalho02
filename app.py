from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        message = data.get("message")

        if not message:
            return jsonify({"error": "Missing 'message'"}), 400

        key = get_random_bytes(32)
        iv = get_random_bytes(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))

        result = {
            "key": base64.b64encode(key).decode(),
            "iv": base64.b64encode(iv).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
