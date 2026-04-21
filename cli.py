"""
Standalone Command Line Interface for Multilingual Translation.
Runs completely standalone - no server required!
"""

import sys
import logging
from typing import Optional
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.translator import MultilingualTranslator
from src.models import LanguagePairRegistry


class TranslationCLI:
    """Interactive CLI for text translation."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.translator: Optional[MultilingualTranslator] = None
        self.is_initialized = False
        self.recent_translations = []
    
    def print_header(self):
        """Print welcome header."""
        print("\n")
        print("=" * 70)
        print("     🌍 MULTILINGUAL TRANSLATION SYSTEM - INTERACTIVE CLI 🌍")
        print("=" * 70)
        print("\n  Powered by MarianMT & Hugging Face Transformers")
        print("  Type 'help' for available commands\n")
    
    def print_help(self):
        """Print help information."""
        help_text = """
Available Commands:
  translate    - Translate text (interactive)
  quick        - Quick translation (specify args: 'quick LANG TEXT')
  supported    - Show supported language pairs
  recent       - Show recent translations
  clear        - Clear recent translations
  help         - Show this help message
  quit/exit    - Exit the program

Examples:
  > translate
  > quick en fr Hello world
  > supported
  > recent
"""
        print(help_text)
    
    def print_supported_languages(self):
        """Show supported language pairs."""
        pairs = LanguagePairRegistry.list_supported_pairs()
        
        print("\n" + "=" * 70)
        print("SUPPORTED LANGUAGE PAIRS")
        print("=" * 70)
        
        # Group by source language
        by_source = {}
        for source, target in pairs:
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(target)
        
        for source in sorted(by_source.keys()):
            targets = by_source[source]
            targets_str = ", ".join(sorted(targets))
            print(f"\n  {source.upper():>5} → {targets_str}")
        
        print("\n" + "=" * 70 + "\n")
    
    def print_recent(self):
        """Show recent translations."""
        if not self.recent_translations:
            print("\n❌ No recent translations. Start translating!\n")
            return
        
        print("\n" + "=" * 70)
        print("RECENT TRANSLATIONS")
        print("=" * 70)
        
        for i, trans in enumerate(self.recent_translations[-10:], 1):
            print(f"\n{i}. [{trans['source_lang'].upper()} → {trans['target_lang'].upper()}]")
            print(f"   Original:    {trans['original'][:60]}...")
            print(f"   Translation: {trans['translation'][:60]}...")
        
        print("\n" + "=" * 70 + "\n")
    
    def initialize_translator(self):
        """Initialize the translator (lazy loading)."""
        if self.is_initialized:
            return
        
        print("\n⏳ Initializing translator (this may take a moment on first run)...")
        print("   Loading models from Hugging Face...\n")
        
        try:
            self.translator = MultilingualTranslator(enable_metrics=False)
            self.is_initialized = True
            print("✓ Translator initialized successfully!\n")
        except Exception as e:
            print(f"\n❌ Error initializing translator: {e}")
            print("   Please check your internet connection and dependencies.\n")
            sys.exit(1)
    
    def validate_language_pair(self, source_lang: str, target_lang: str) -> bool:
        """Validate language pair."""
        if not LanguagePairRegistry.is_supported(source_lang, target_lang):
            print(f"\n❌ Unsupported language pair: {source_lang.upper()} → {target_lang.upper()}")
            print(f"   Run 'supported' to see available pairs.\n")
            return False
        return True
    
    def translate_interactive(self):
        """Interactive translation mode."""
        self.initialize_translator()
        
        print("\n" + "-" * 70)
        print("INTERACTIVE TRANSLATION MODE")
        print("-" * 70)
        print("(Type 'back' to return to main menu)\n")
        
        while True:
            try:
                # Get source language
                source_lang = input("Enter source language code (e.g., 'en'): ").strip().lower()
                if source_lang == 'back':
                    break
                if not source_lang:
                    print("❌ Language code cannot be empty.\n")
                    continue
                
                # Get target language
                target_lang = input("Enter target language code (e.g., 'fr'): ").strip().lower()
                if target_lang == 'back':
                    break
                if not target_lang:
                    print("❌ Language code cannot be empty.\n")
                    continue
                
                # Validate pair
                if not self.validate_language_pair(source_lang, target_lang):
                    continue
                
                # Get text to translate
                text = input(f"Enter text to translate ({source_lang.upper()}→{target_lang.upper()}): ").strip()
                if text == 'back':
                    break
                if not text:
                    print("❌ Text cannot be empty.\n")
                    continue
                
                # Translate
                self.perform_translation(text, source_lang, target_lang)
                
                # Ask if continue
                cont = input("\nTranslate another? (y/n): ").strip().lower()
                if cont != 'y':
                    break
                print()
            
            except KeyboardInterrupt:
                print("\n\n⏸  Interrupted by user.\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")
    
    def perform_translation(self, text: str, source_lang: str, target_lang: str):
        """Perform translation and display results."""
        try:
            print(f"\n⏳ Translating... ", end="", flush=True)
            
            result = self.translator.translate(
                text,
                source_lang,
                target_lang,
                return_full_result=True
            )
            
            # Store in recent
            self.recent_translations.append({
                'original': text,
                'translation': result['translation'],
                'source_lang': source_lang,
                'target_lang': target_lang,
            })
            
            # Display result
            print("✓")
            print("\n" + "─" * 70)
            print(f"📝 Original ({source_lang.upper()}):")
            print(f"   {result['original']}")
            print(f"\n✨ Translation ({target_lang.upper()}):")
            print(f"   {result['translation']}")
            print("─" * 70)
        
        except ValueError as e:
            print(f"\n❌ Invalid input: {e}\n")
        except Exception as e:
            print(f"\n❌ Translation error: {e}\n")
    
    def quick_translate(self, args: list):
        """Quick translation from command arguments."""
        if len(args) < 3:
            print("\n❌ Usage: quick <target_lang> <text>")
            print("   Example: quick fr Hello world\n")
            return
        
        target_lang = args[1].strip().lower()
        text = " ".join(args[2:]).strip()
        
        self.initialize_translator()
        
        if not self.validate_language_pair('en', target_lang):
            return
        
        self.perform_translation(text, 'en', target_lang)
        print()
    
    def run(self):
        """Main CLI loop."""
        self.print_header()
        
        while True:
            try:
                cmd = input("🔷 Enter command: ").strip().lower()
                
                if not cmd:
                    continue
                
                if cmd == 'translate':
                    self.translate_interactive()
                
                elif cmd == 'supported':
                    self.print_supported_languages()
                
                elif cmd == 'recent':
                    self.print_recent()
                
                elif cmd == 'clear':
                    self.recent_translations = []
                    print("\n✓ Recent translations cleared.\n")
                
                elif cmd == 'help':
                    self.print_help()
                
                elif cmd.startswith('quick '):
                    args = cmd.split()
                    self.quick_translate(args)
                
                elif cmd in ['quit', 'exit']:
                    print("\n👋 Goodbye! Happy translating!\n")
                    break
                
                else:
                    print(f"\n❌ Unknown command: '{cmd}'")
                    print("   Type 'help' for available commands.\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def main():
    """Entry point."""
    cli = TranslationCLI()
    cli.run()


if __name__ == "__main__":
    main()
