from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota GET


@app.route('/api/get_example', methods=['GET'])
def get_example():
    data = {"message": "Este é um exemplo de solicitação GET."}
    return jsonify(data)

# Rota POST


@app.route('/api/post_example', methods=['POST'])
def post_example():
    data = request.get_json()  # Obtém os dados JSON da solicitação POST
    if data is None:
        return jsonify({"error": "Dados JSON ausentes na solicitação."}), 400
    message = data.get("message")
    if message:
        return jsonify({"message": f"Você enviou uma mensagem via POST: {message}"})
    else:
        return jsonify({"error": "Nenhuma mensagem encontrada nos dados JSON da solicitação."}), 400


if __name__ == '__main__':
    app.run(debug=True)
