"""
Quick demo script showing translations without interactive input.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.translator import MultilingualTranslator


def demo():
    """Run translation demo."""
    print("\n" + "="*70)
    print("  🌍 MULTILINGUAL TRANSLATION DEMO 🌍")
    print("="*70 + "\n")
    
    print("Initializing translator...")
    translator = MultilingualTranslator(enable_metrics=False)
    
    # Demo translations
    demos = [
        ("Hello, how are you?", "en", "fr", "French"),
        ("Hello, how are you?", "en", "de", "German"),
        ("Hello, how are you?", "en", "es", "Spanish"),
        ("Good morning!", "en", "it", "Italian"),
        ("Thank you very much!", "en", "pt", "Portuguese"),
    ]
    
    print("✓ Translator initialized!\n")
    print("="*70)
    print("  TRANSLATION EXAMPLES")
    print("="*70 + "\n")
    
    for i, (text, source, target, lang_name) in enumerate(demos, 1):
        try:
            print(f"Example {i}: Translating to {lang_name}")
            print(f"  Original ({source.upper()}): {text}")
            
            translation = translator.translate(text, source, target)
            print(f"  {lang_name:>12}:  {translation}")
            print()
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
    
    print("="*70)
    print("\n✓ Demo complete!")
    print("\n📝 To use interactively, run: python cli.py\n")


if __name__ == "__main__":
    demo()
