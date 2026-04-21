"""
Batch translation example showing processing multiple texts.
"""

from src.translator import MultilingualTranslator


def main():
    """Batch translation example."""
    
    # Initialize translator
    print("Initializing translator with metrics...")
    translator = MultilingualTranslator(enable_metrics=True)
    
    # Sample texts for batch translation
    texts = [
        "The weather is beautiful today.",
        "I love learning new languages.",
        "Machine translation is fascinating.",
        "Technology is advancing rapidly.",
        "What time is the meeting tomorrow?",
    ]
    
    print(f"\nBatch translating {len(texts)} texts from English to French\n")
    
    for i, text in enumerate(texts, 1):
        print(f"{i}. Original: {text}")
    
    # Translate all texts
    try:
        translations = translator.translate_batch(
            texts, "en", "fr", batch_size=5
        )
        
        print("\n--- Translated Results ---\n")
        for original, translation in zip(texts, translations):
            print(f"EN: {original}")
            print(f"FR: {translation}")
            print()
    
    except Exception as e:
        print(f"Error: {e}")
    
    # Print performance metrics
    print("\n--- Performance Metrics ---")
    metrics = translator.get_metrics()
    if metrics:
        print(f"Total translations: {metrics['translation_count']}")
        print(f"Average time: {metrics['avg_time_ms']:.2f} ms")
        print(f"Total time: {metrics['total_time_ms']:.2f} ms")
        print(f"Total tokens: {metrics['total_tokens']}")
        print(f"Tokens/sec: {metrics['tokens_per_sec']:.2f}")
    
    # Show supported language pairs
    print("\n--- Supported Language Pairs from English ---")
    supported = translator.get_supported_languages()
    if 'en' in supported:
        print(f"From English to: {', '.join(supported['en'][:5])}...")


if __name__ == "__main__":
    main()
