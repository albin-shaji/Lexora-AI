import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# --- Gemini API Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set it in a .env file.")

genai.configure(api_key=GEMINI_API_KEY)
text_model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
# --- End Gemini Configuration ---

@app.route('/')
def home():
    """Render the main page (index.html)"""
    return render_template('index.html')

@app.route('/how-lexora-works')
def how_lexora_works():
    """Render the How Lexora Works page"""
    return render_template('how_lexora_works.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    """
    API endpoint to handle translation requests.
    Expects JSON: { q: text, source: sourceLang, target: targetLang }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON input.'}), 400

        text_to_translate = data.get('q')
        source_lang_code = data.get('source')
        target_lang_code = data.get('target')

        if not all([text_to_translate, source_lang_code, target_lang_code]):
            return jsonify({'error': 'Missing required fields.'}), 400

        # Supported languages
        languages = {
            'en': 'English', 'es': 'Spanish', 'fr': 'French', 'de': 'German',
            'it': 'Italian', 'pt': 'Portuguese', 'nl': 'Dutch', 'ru': 'Russian',
            'ja': 'Japanese', 'ko': 'Korean', 'zh': 'Chinese', 'ar': 'Arabic',
            'hi': 'Hindi', 'bn': 'Bengali', 'ta': 'Tamil', 'te': 'Telugu',
            'kn': 'Kannada', 'ml': 'Malayalam', 'ur': 'Urdu', 'sv': 'Swedish',
            'pl': 'Polish', 'tr': 'Turkish', 'vi': 'Vietnamese'
        }

        source_lang_name = 'the detected language' if source_lang_code == 'auto' else languages.get(source_lang_code, source_lang_code)
        target_lang_name = languages.get(target_lang_code, target_lang_code)

        # Prompt Engineering
        prompt = (
            f"Translate the following text from {source_lang_name} to {target_lang_name}. "
            "Only provide the translated text, without any additional commentary.\n\n"
            f"Text: \"{text_to_translate}\""
        )

        response = text_model.generate_content(prompt)
        if response.candidates:
            translated_text = response.candidates[0].content.parts[0].text.strip()
            detected_lang_info = "Auto-Detected" if source_lang_code == 'auto' else source_lang_name
            return jsonify({'text': translated_text, 'detectedLang': detected_lang_info})
        else:
            return jsonify({'text': 'Error: Translation failed.', 'detectedLang': 'error'}), 500

    except Exception as e:
        print(f"Error during translation: {e}")
        return jsonify({'text': 'Internal server error.', 'detectedLang': 'error'}), 500

# if __name__ == '__main__':
#     # Run Flask in debug mode
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='127.0.0.5', port=80, debug=True)