
from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
import os

app = Flask(__name__)

# Supported language models
models = {
    'ha': 'Helsinki-NLP/opus-mt-en-ha',
    'yo': 'Helsinki-NLP/opus-mt-en-yo',
    'ig': 'Helsinki-NLP/opus-mt-en-ig',
    'ar': 'Helsinki-NLP/opus-mt-en-ar'
}

loaded_models = {}
tokenizers = {}

# Load models and tokenizers
for lang_code, model_name in models.items():
    tokenizers[lang_code] = MarianTokenizer.from_pretrained(model_name)
    loaded_models[lang_code] = MarianMTModel.from_pretrained(model_name)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'ha')
    
    if not text or target_lang not in models:
        return jsonify({'error': 'Invalid input'}), 400

    tokenizer = tokenizers[target_lang]
    model = loaded_models[target_lang]
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
