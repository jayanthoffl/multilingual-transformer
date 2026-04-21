# Multilingual Translation System

A comprehensive multilingual translation system using Python, MarianMT models, and Hugging Face Transformers. Translate text between 20+ language pairs with high-quality neural machine translation.

## Features

✨ **Core Features:**
- 🌍 **Multi-language Support**: Support for 20+ language pairs (English, French, German, Spanish, Italian, Portuguese, Russian, Japanese, Chinese, and more)
- 🚀 **Fast Translation**: Batch processing for efficient translation of multiple texts
- 📊 **Performance Metrics**: Track translation time, tokens processed, and throughput
- 💾 **Model Caching**: Automatic model caching to improve performance
- 🔧 **Flexible API**: Simple Python API and REST API server
- 📱 **Cross-platform**: Works on CPU, CUDA GPU, and Apple Silicon (MPS)

## Architecture

```
multilingual_translator/
├── src/
│   ├── __init__.py
│   ├── translator.py      # Main translation class
│   ├── models.py          # Model loading and management
│   └── utils.py           # Utility functions
├── examples/
│   ├── simple_translation.py   # Basic usage
│   ├── batch_translation.py    # Batch processing
│   └── server.py               # Flask API server
├── tests/
│   └── test_translator.py      # Unit tests
├── config/
│   └── config.yaml        # Configuration
├── requirements.txt       # Dependencies
└── README.md
```

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Clone or download the project:**
```bash
cd multilingual_translator
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

> **Note**: First run will download ~1.5GB of models from Hugging Face Hub. Subsequent runs will use cached models.

## Quick Start

### Simple Translation

```python
from src.translator import MultilingualTranslator

# Initialize translator
translator = MultilingualTranslator()

# Translate text
text = "Hello, how are you today?"
translation = translator.translate(text, "en", "fr")
print(translation)  # "Bonjour, comment allez-vous aujourd'hui?"
```

### Batch Translation

```python
texts = [
    "The weather is beautiful today.",
    "I love learning new languages.",
    "Machine translation is fascinating.",
]

translations = translator.translate_batch(texts, "en", "de")
for orig, trans in zip(texts, translations):
    print(f"{orig} -> {trans}")
```

### Get Full Result

```python
result = translator.translate(
    "Hello world",
    "en", "es",
    return_full_result=True
)
print(result)
# {
#     'original': 'Hello world',
#     'translation': 'Hola mundo',
#     'source_language': 'en',
#     'target_language': 'es',
#     'confidence': 1.0
# }
```

## 🚀 QUICK START (3 STEPS)

### Step 1: Navigate to the project
```powershell
cd d:\PROJECTS\multilingual_translator
```

### Step 2: Run the interactive CLI
```powershell
python cli.py
```

### Step 3: Start translating!
```
🔷 Enter command: translate
Enter source language code (e.g., 'en'): en
Enter target language code (e.g., 'fr'): fr
Enter text to translate: Hello, how are you?
```

---

## 📋 CLI COMMANDS

Inside the CLI, you can use these commands:

| Command | Description | Example |
|---------|-------------|---------|
| `translate` | Interactive translation mode | `translate` |
| `quick` | Quick translation (English by default) | `quick fr Hello world` |
| `supported` | Show all supported language pairs | `supported` |
| `recent` | Show last 10 translations | `recent` |
| `clear` | Clear translation history | `clear` |
| `help` | Show help message | `help` |
| `quit` or `exit` | Exit the program | `quit` |

---

## 🎯 EXAMPLES

### Example 1: Interactive Translation
```
🔷 Enter command: translate
Enter source language code (e.g., 'en'): en
Enter target language code (e.g., 'fr'): fr
Enter text to translate: Good morning!
⏳ Translating... ✓

──────────────────────────────────────────────────────────
📝 Original (EN):
   Good morning!

✨ Translation (FR):
   Bonjour!
──────────────────────────────────────────────────────────

Translate another? (y/n): n
```

### Example 2: Quick Translation
```
🔷 Enter command: quick es Beautiful weather today

⏳ Translating... ✓

──────────────────────────────────────────────────────────
📝 Original (EN):
   Beautiful weather today

✨ Translation (ES):
   Hermoso clima hoy
──────────────────────────────────────────────────────────
```

### Example 3: View Supported Languages
```
🔷 Enter command: supported

════════════════════════════════════════════════════════════════════
SUPPORTED LANGUAGE PAIRS
════════════════════════════════════════════════════════════════════

      de → en, es, fr, it, pt
      en → de, es, fr, it, ja, pt, ru, zh
      es → de, en, fr
      fr → de, en, es, it, pt, ru
      it → en, pt
      ja → en
      pt → en, es, fr, it, ru
      ru → en, fr, pt
      zh → en
```

### Example 4: View Recent Translations
```
🔷 Enter command: recent

════════════════════════════════════════════════════════════════════
RECENT TRANSLATIONS
════════════════════════════════════════════════════════════════════

1. [EN → FR]
   Original:    Hello, how are you?
   Translation: Bonjour, comment allez-vous?

2. [EN → DE]
   Original:    Good morning!
   Translation: Guten Morgen!
```

---

## 📌 ALTERNATIVE USAGE METHODS

### Method 1: Run Demo (No interaction)
```powershell
python demo.py
```
Shows 5 example translations without user input.

### Method 2: Python Script
Create a file `my_translation.py`:
```python
from src.translator import MultilingualTranslator

translator = MultilingualTranslator()
result = translator.translate("Hello world", "en", "fr")
print(result)
```

Then run:
```powershell
python my_translation.py
```

### Method 3: Run Diagnostic
```powershell
python diagnose.py
```
Checks system status and setup.

### Method 4: Run Tests
```powershell
pytest tests\ -v
```
Runs unit tests to verify functionality.

---

## 🌍 SUPPORTED LANGUAGE CODES

| Code | Language |
|------|----------|
| `en` | English |
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `it` | Italian |
| `pt` | Portuguese |
| `ru` | Russian |
| `ja` | Japanese |
| `zh` | Chinese |

---

## 📊 LANGUAGE PAIRS AVAILABLE

All combinations marked with ✓:

```
     de    en    es    fr    it    ja    pt    ru    zh
de   -     ✓     ✓     ✓     -     -     -     -     -
en   ✓     -     ✓     ✓     ✓     ✓     ✓     ✓     ✓
es   ✓     ✓     -     ✓     -     -     -     -     -
fr   ✓     ✓     ✓     -     ✓     -     ✓     ✓     -
it   -     ✓     -     ✓     -     -     ✓     -     -
ja   -     ✓     -     -     -     -     -     -     -
pt   -     ✓     -     ✓     ✓     -     -     ✓     -
ru   -     ✓     -     ✓     -     -     ✓     -     -
zh   -     ✓     -     -     -     -     -     -     -
```

---

## ⚠️ IMPORTANT NOTES

### First Time Setup
- **Initial download**: First translation will download ~500MB of model files
- **Time**: First translation takes 30-60 seconds (subsequent translations are faster)
- **Internet required**: Need internet connection for first run only

### Performance Tips
1. **Use GPU if available**: Much faster than CPU (10x+ speedup)
2. **Batch processing**: Translating multiple texts is more efficient
3. **Reuse translator**: Initialize once, translate multiple times
4. **Model caching**: Models are automatically cached after first download

### Memory Usage
- **Base**: ~2GB RAM
- **Per model**: ~500MB
- **Batch processing**: Scales with batch size (default: 32 texts)

---

## 🐛 TROUBLESHOOTING

### "Module not found" Error
```powershell
pip install -r requirements.txt
```

### "Connection Error" / Can't download models
- Check internet connection
- Models download from Hugging Face
- Try again after connection is restored

### Very Slow Translation
- Normal on first run (model loading)
- Subsequent runs are much faster
- Use GPU if you have CUDA installed

### Out of Memory
- Reduce batch size
- Use CPU instead of GPU
- Close other applications

### Run Diagnostic
```powershell
python diagnose.py
```
This checks your system and shows any issues.

---

## 📁 PROJECT STRUCTURE

```
multilingual_translator/
├── src/
│   ├── __init__.py          # Package init
│   ├── translator.py        # Main translator class
│   ├── models.py            # Model management
│   └── utils.py             # Utility functions
├── examples/                # Example scripts
├── tests/                   # Unit tests
├── cli.py                   # ← USE THIS! Interactive CLI
├── demo.py                  # Demo script
├── diagnose.py              # System diagnostics
├── requirements.txt         # Dependencies
└── README.md                # Full documentation
```

---

## 🔧 FEATURES

✓ **Multi-language Support**: 20+ language pairs  
✓ **Batch Translation**: Translate multiple texts  
✓ **Fast Caching**: Models cached for speed   
✓ **GPU Support**: CUDA acceleration available  
✓ **Error Handling**: Clear error messages  
✓ **Performance Metrics**: Track translation speed  
✓ **Easy CLI**: Simple command-line interface  
✓ **Python API**: Use in your scripts  
✓ **Cross-platform**: Windows, Mac, Linux  

---

## 🎓 LEARNING RESOURCES

- `README.md`: Full technical documentation
- `src/translator.py`: Main class implementation
- `examples/`: Example scripts for reference
- `tests/`: Unit tests showing usage patterns

---

## 💡 NEXT STEPS

1. **✅ Run the CLI**: `python cli.py`
2. **📝 Try translating**: Use the `translate` command
3. **🌍 Explore languages**: Use `supported` command
4. **📖 Read docs**: Check `README.md` for advanced features
5. **🧪 Run tests**: Verify with `pytest tests\ -v`

---

## ❓ QUESTIONS?

- Check `diagnose.py` output
- Run `python cli.py` then type `help`
- Read `README.md` for technical details
- Look at `examples/` folder for code samples

---

**Status**: ✅ Ready to use!  
**Last Updated**: April 22, 2026  
**Version**: 1.0.0

Enjoy your multilingual translator! 🌍


### Performance Metrics

```python
translator = MultilingualTranslator(enable_metrics=True)
translator.translate("Hello world", "en", "fr")

metrics = translator.get_metrics()
print(f"Tokens/sec: {metrics['tokens_per_sec']:.2f}")
print(f"Average time: {metrics['avg_time_ms']:.2f}ms")
```

## Usage Examples

### Run Simple Example
```bash
python examples/simple_translation.py
```

### Run Batch Translation Example
```bash
python examples/batch_translation.py
```

### Start API Server
```bash
python examples/server.py
```

Then in another terminal, test with curl:
```bash
# Translate single text
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "source_lang": "en", "target_lang": "fr"}'

# Translate multiple texts
curl -X POST http://localhost:5000/batch-translate \
  -H "Content-Type: application/json" \
  -d '{
    "texts": ["Hello", "Goodbye"],
    "source_lang": "en",
    "target_lang": "de"
  }'

# Get supported languages
curl http://localhost:5000/supported-languages

# Get metrics
curl http://localhost:5000/metrics

# Health check
curl http://localhost:5000/health
```

## API Documentation

### MultilingualTranslator Class

#### Methods

**`__init__(device=None, cache_dir=None, enable_metrics=False)`**
- Initialize the translator
- `device`: 'cpu', 'cuda', or 'mps' (auto-detect if None)
- `cache_dir`: Directory to cache models
- `enable_metrics`: Enable performance tracking

**`translate(text, source_lang, target_lang, batch_size=32, return_full_result=False)`**
- Translate single text
- Returns translated text or full result dict

**`translate_batch(texts, source_lang, target_lang, batch_size=32)`**
- Translate multiple texts
- Returns list of translations

**`get_supported_languages()`**
- Get supported language pairs
- Returns dict mapping source languages to target languages

**`get_metrics()`**
- Get performance metrics
- Returns dict with translation statistics

**`clear_cache()`**
- Clear model cache to free memory

## Supported Language Pairs

| Source | Targets |
|--------|---------|
| en | fr, de, es, it, pt, ru, ja, zh |
| fr | en, de, es |
| de | en, fr, es |
| es | en, fr, de |
| it | en |
| pt | en |
| ru | en |
| ja | en |
| zh | en |

*See `LanguagePairRegistry.SUPPORTED_PAIRS` for complete list*

## Model Information

- **Models**: Helsinki-NLP/opus-mt-* (OPUS-MT)
- **Training**: Trained on large parallel corpora
- **Size**: ~350MB per model (varies by language pair)
- **Quality**: State-of-the-art neural machine translation

## Performance

### Benchmarks (CPU, i7, estimate)
- Single sentence (en->fr): ~200-500ms (first run with model loading)
- Single sentence (en->fr): ~20-50ms (subsequent runs with cached model)
- Batch of 10 sentences: ~100-200ms
- Throughput: 50-100 tokens/sec (CPU), 500+ tokens/sec (GPU)

### Tips for Optimization
1. Use GPU if available for better performance
2. Enable batch processing for multiple texts
3. Reuse translator instance to benefit from model caching
4. Use appropriate batch sizes (32 is default, adjust based on memory)

## Testing

Run unit tests:
```bash
pytest tests/ -v
```

Run specific test:
```bash
pytest tests/test_translator.py::TestUtilityFunctions -v
```

## Troubleshooting

### Out of Memory Error
- Reduce batch_size parameter
- Use CPU instead of GPU
- Clear cache: `translator.clear_cache()`

### Model Download Issues
- Check internet connection
- Try clearing Hugging Face cache: `rm -rf ~/.cache/huggingface/`
- Manually download model: `transformers-cli download Helsinki-NLP/opus-mt-en-fr`

### Slow First Translation
- This is normal! First translation loads the model from disk
- Use batch processing for better throughput
- Consider preloading models during initialization

## Advanced Usage

### Custom Configuration

```python
from src.translator import MultilingualTranslator

translator = MultilingualTranslator(
    device='cuda',  # Use GPU
    cache_dir='/path/to/models',
    enable_metrics=True
)

# Translate with custom batch size
result = translator.translate(
    "Hello world",
    "en", "fr",
    batch_size=64  # Larger batches
)
```

### Integration with Applications

```python
# Web application integration
app_translator = MultilingualTranslator()

def translate_user_input(text, target_lang):
    try:
        return app_translator.translate(text, "en", target_lang)
    except ValueError as e:
        return f"Translation error: {e}"
```

## Dependencies

- **torch**: Deep learning framework
- **transformers**: Hugging Face transformer models
- **sentencepiece**: Tokenization
- **flask**: REST API framework (optional, for server example)
- **pytest**: Testing framework (optional)

See `requirements.txt` for all dependencies and versions.

## Project Structure

```
src/
├── translator.py      # Main MultilingualTranslator class
├── models.py          # ModelManager and LanguagePairRegistry
└── utils.py           # Utility functions and metrics

examples/
├── simple_translation.py   # Basic usage example
├── batch_translation.py    # Batch processing example
└── server.py               # Flask REST API server

tests/
└── test_translator.py      # Unit tests

config/
└── config.yaml             # Configuration file
```

## Key Classes

### MultilingualTranslator
Main class for text translation. Handles model loading, batch processing, and metrics tracking.

### ModelManager
Manages loading and caching of transformer models. Supports automatic device detection.

### LanguagePairRegistry
Registry of supported language pairs and their corresponding models.

### PerformanceMetrics
Tracks translation performance metrics (time, throughput, tokens).

## Future Enhancements

- [ ] Language detection
- [ ] Fine-tuning on domain-specific data
- [ ] Back-translation scoring
- [ ] Real-time streaming translation
- [ ] Docker containerization
- [ ] Multi-GPU support
- [ ] Quantized models for faster inference
- [ ] Vocabulary switching

## License

This project uses open-source models and libraries. See individual licenses:
- Transformers: Apache 2.0
- Torch: BSD
- Helsinki-NLP Models: Attribution-ShareAlike 4.0

## References

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OPUS-MT Models](https://huggingface.co/Helsinki-NLP)
- [MarianMT Paper](https://arxiv.org/abs/2104.06431)
- [PyTorch](https://pytorch.org/)

## Contributing

Contributions welcome! Areas for improvement:
- Additional language pairs
- Performance optimizations
- Better error handling
- Documentation improvements

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review example scripts
3. Run tests to verify installation
4. Check Hugging Face documentation



---

**Created**: 2026
**Status**: Production Ready
