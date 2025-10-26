Lexora - The AI Translator

Lexora is a sleek, fast, and modern web application that provides high-quality, context-aware translations. It's powered by a Python Flask backend and Google's advanced Gemini AI model.

This project serves as a complete example of how to build a full-stack application that connects a modern user interface to a powerful Large Language Model (LLM) for a real-world task.

Features

AI-Powered Translations: Utilizes Google's gemini-2.5-flash-preview-09-2025 model for nuanced and accurate translations.

Multi-Language Support: Supports a wide range of languages, including English, Spanish, French, German, Japanese, Hindi, and many more.

Auto-Detect Language: Can automatically detect the source language.

Intuitive UI:

Clean, responsive design built with Tailwind CSS.

Dark mode support (syncs with system preference or manual toggle).

Character count with a 5000-character limit.

Utility Features:

Swap Languages: Instantly swap source and target languages.

Copy & Paste: Easily copy source/translated text or paste from your clipboard.

Download: Save your translation as a .txt file.

Clear Text: Reset the text areas with one click.

Informative "How it Works" Page: A dedicated page (/how-lexora-works) that breaks down the application's architecture.

How It Works

Lexora's architecture is a simple, effective full-stack model:

Frontend (Client): The user interacts with the index.html page. All UI logic (like dark mode, character counting, and button clicks) is handled by plain JavaScript.

API Request: When the "Translate" button is clicked (or after the user stops typing), the frontend JavaScript sends a POST request to the backend's /translate endpoint. This request contains the text to be translated, the source language, and the target language.

Backend (Server): A Python Flask server running in app.py receives the request. It securely retrieves the GEMINI_API_KEY from its environment.

Prompt Engineering: The backend constructs a specific prompt for the Gemini model, telling it exactly what to translate and to only return the translated text.

AI Engine: The backend sends this prompt to the Google Gemini API.

Response: The Gemini API returns the translated text, which the Flask server then sends back to the frontend as a JSON response. The JavaScript on the page displays this translation in the output box.

Technology Stack

Backend: Python with Flask

Frontend: HTML, Tailwind CSS, and plain JavaScript (ES6+)

AI Model: Google's Gemini API (gemini-2.5-flash-preview-09-2025)

Dependencies: google-generativeai, python-dotenv

Setup and Installation

To run this project locally, follow these steps:

Create a Python Virtual Environment

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate


Install Dependencies
A requirements.txt file is included. Install all dependencies using pip:

pip install -r requirements.txt


Create a .env File
Create a file named .env in the root of the project directory. This file will securely store your API key.

GEMINI_API_KEY=YOUR_API_KEY_GOES_HERE


Replace YOUR_API_KEY_GOES_HERE with your actual Google Gemini API key.

Run the Application

python app.py


The application will be running at http://127.0.0.5:80 (or as specified in app.py).

Credits

Designed and Crafted with ❤️ from Team Green Gala

Mohammed Shan S

Abhinav Sankar

Albin Shaji

Alen Thomas

Jaison George
