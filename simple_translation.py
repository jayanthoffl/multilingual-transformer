"""
Simple example showing basic translation.
"""

from src.translator import MultilingualTranslator


def main():
    """Basic translation example."""
    
    # Initialize translator
    print("Initializing translator...")
    translator = MultilingualTranslator(enable_metrics=True)
    
    # Simple translation
    text = "Hello, how are you today?"
    print(f"\nOriginal text: {text}")
    
    # Translate English to French
    print("\n--- Translating to French ---")
    try:
        translated_fr = translator.translate(text, "en", "fr")
        print(f"French: {translated_fr}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Translate English to German
    print("\n--- Translating to German ---")
    try:
        translated_de = translator.translate(text, "en", "de")
        print(f"German: {translated_de}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Translate English to Spanish
    print("\n--- Translating to Spanish ---")
    try:
        translated_es = translator.translate(text, "en", "es")
        print(f"Spanish: {translated_es}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Get full result
    print("\n--- Full Result (en -> fr) ---")
    try:
        full_result = translator.translate(
            text, "en", "fr", return_full_result=True
        )
        for key, value in full_result.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Print metrics
    print("\n--- Performance Metrics ---")
    metrics = translator.get_metrics()
    if metrics:
        for key, value in metrics.items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")


if __name__ == "__main__":
    main()
