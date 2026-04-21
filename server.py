"""
Advanced example showing Flask API server for translations.
"""

from flask import Flask, request, jsonify
import logging
from src.translator import MultilingualTranslator
from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this line
import logging
from src.translator import MultilingualTranslator

app = Flask(__name__)
CORS(app)  # Add this line

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global translator instance
translator = None


def init_translator():
    """Initialize the translator on app startup."""
    global translator
    logger.info("Initializing translator...")
    translator = MultilingualTranslator(enable_metrics=True)
    logger.info("Translator initialized successfully")


@app.route('/translate', methods=['POST'])
def translate():
    """Endpoint to translate text."""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field"}), 400
        
        text = data.get('text', '')
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'fr')
        
        if not text:
            return jsonify({"error": "Text cannot be empty"}), 400
        
        # Perform translation
        translation = translator.translate(
            text, source_lang, target_lang, return_full_result=True
        )
        
        return jsonify(translation), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({"error": "Translation failed"}), 500


@app.route('/batch-translate', methods=['POST'])
def batch_translate():
    """Endpoint to translate multiple texts."""
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({"error": "Missing 'texts' field"}), 400
        
        texts = data.get('texts', [])
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'fr')
        
        if not texts or not isinstance(texts, list):
            return jsonify({"error": "Texts must be a non-empty list"}), 400
        
        # Perform batch translation
        translations = translator.translate_batch(
            texts, source_lang, target_lang
        )
        
        results = [
            {
                "original": orig,
                "translation": trans,
                "source_language": source_lang,
                "target_language": target_lang,
            }
            for orig, trans in zip(texts, translations)
        ]
        
        return jsonify({"results": results}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Batch translation error: {str(e)}")
        return jsonify({"error": "Batch translation failed"}), 500


@app.route('/supported-languages', methods=['GET'])
def supported_languages():
    """Get supported language pairs."""
    try:
        languages = translator.get_supported_languages()
        return jsonify({"supported_pairs": languages}), 200
    except Exception as e:
        logger.error(f"Error getting supported languages: {str(e)}")
        return jsonify({"error": "Failed to get supported languages"}), 500


@app.route('/metrics', methods=['GET'])
def metrics():
    """Get performance metrics."""
    try:
        metrics_data = translator.get_metrics()
        return jsonify({"metrics": metrics_data}), 200
    except Exception as e:
        logger.error(f"Error getting metrics: {str(e)}")
        return jsonify({"error": "Failed to get metrics"}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    init_translator()
    print("\n" + "="*50)
    print("Translation API Server")
    print("="*50)
    print("\nAvailable endpoints:")
    print("  POST /translate - Translate single text")
    print("  POST /batch-translate - Translate multiple texts")
    print("  GET /supported-languages - List supported language pairs")
    print("  GET /metrics - Get performance metrics")
    print("  GET /health - Health check")
    print("\nExample request:")
    print('''curl -X POST http://localhost:5000/translate \\
  -H "Content-Type: application/json" \\
  -d '{"text": "Hello", "source_lang": "en", "target_lang": "fr"}'
''')
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
