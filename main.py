from flask import Flask, request, jsonify
from google import genai

# Inicializa Flask
app = Flask(__name__)

# Inicializa cliente de Gemini con tu API key
client = genai.Client(api_key='AIzaSyAAgfgQqKushcG6VUoE-F6odZ4wO9P4_Po')


@app.route('/prompt', methods=['POST'])
def prompt_handler():
    # Obtiene el JSON recibido
    data = request.get_json()

    # Valida que venga el campo 'prompt'
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Falta el campo "prompt" en el cuerpo del POST.'}), 400

    prompt = data['prompt']

    try:
        print('Pensando...')
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # asegúrate del nombre del modelo
            contents="tienes siempre que dar respuestas resumidas, aqui tienes el prompt: " + prompt
        )
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
