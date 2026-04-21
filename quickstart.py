"""
Quick start guide for the multilingual translation system.
Run this script to test the basic functionality.
"""

import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_installation():
    """Test if all required packages are installed."""
    print("\n" + "="*60)
    print("TESTING INSTALLATION")
    print("="*60 + "\n")
    
    required_packages = {
        'torch': 'PyTorch',
        'transformers': 'Hugging Face Transformers',
        'sentencepiece': 'SentencePiece',
        'click': 'Click',
        'pyyaml': 'PyYAML',
    }
    
    missing = []
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name} is installed")
        except ImportError:
            print(f"✗ {name} is NOT installed")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print(f"\nInstall with: pip install {' '.join(missing)}")
        return False
    else:
        print("\n✓ All required packages installed!")
        return True


def test_imports():
    """Test if translation module can be imported."""
    print("\n" + "="*60)
    print("TESTING MODULE IMPORTS")
    print("="*60 + "\n")
    
    try:
        from src.translator import MultilingualTranslator
        from src.models import ModelManager, LanguagePairRegistry
        from src.utils import preprocess_text, validate_language_code
        
        print("✓ Successfully imported all modules")
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False


def test_language_registry():
    """Test language pair registry."""
    print("\n" + "="*60)
    print("TESTING LANGUAGE PAIR REGISTRY")
    print("="*60 + "\n")
    
    try:
        from src.models import LanguagePairRegistry
        
        # Test supported pairs
        pairs = LanguagePairRegistry.list_supported_pairs()
        print(f"✓ Found {len(pairs)} supported language pairs")
        
        # Test specific pairs
        test_pairs = [("en", "fr"), ("en", "de"), ("en", "es")]
        for source, target in test_pairs:
            if LanguagePairRegistry.is_supported(source, target):
                print(f"  ✓ {source} -> {target} is supported")
            else:
                print(f"  ✗ {source} -> {target} is NOT supported")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_utilities():
    """Test utility functions."""
    print("\n" + "="*60)
    print("TESTING UTILITY FUNCTIONS")
    print("="*60 + "\n")
    
    try:
        from src.utils import (
            preprocess_text,
            split_into_sentences,
            batch_texts,
            validate_language_code,
        )
        
        # Test preprocessing
        text = "   Hello   world   "
        cleaned = preprocess_text(text)
        assert cleaned == "Hello world", "Preprocess failed"
        print("✓ Text preprocessing works")
        
        # Test sentence splitting
        text = "Hello. World! How are you?"
        sentences = split_into_sentences(text)
        assert len(sentences) >= 2, "Sentence splitting failed"
        print("✓ Sentence splitting works")
        
        # Test batching
        texts = list(range(10))
        batches = batch_texts(texts, batch_size=3)
        assert len(batches) == 4, "Batching failed"
        print("✓ Text batching works")
        
        # Test language code validation
        assert validate_language_code("en") is True, "Language validation failed"
        assert validate_language_code("invalid") is False, "Language validation failed"
        print("✓ Language code validation works")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def check_project_structure():
    """Verify project structure."""
    print("\n" + "="*60)
    print("VERIFYING PROJECT STRUCTURE")
    print("="*60 + "\n")
    
    required_files = [
        'src/__init__.py',
        'src/translator.py',
        'src/models.py',
        'src/utils.py',
        'examples/simple_translation.py',
        'examples/batch_translation.py',
        'examples/server.py',
        'tests/test_translator.py',
        'config/config.yaml',
        'README.md',
        'requirements.txt',
    ]
    
    missing = []
    for file_path in required_files:
        full_path = Path(file_path)
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} is MISSING")
            missing.append(file_path)
    
    if missing:
        print(f"\n❌ Missing files: {missing}")
        return False
    else:
        print("\n✓ All required files present!")
        return True


def show_next_steps():
    """Show next steps for using the system."""
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60 + "\n")
    
    steps = [
        "1. Install dependencies (if not done):",
        "   pip install -r requirements.txt",
        "",
        "2. Try simple example:",
        "   python examples/simple_translation.py",
        "",
        "3. Try batch translation:",
        "   python examples/batch_translation.py",
        "",
        "4. Start API server:",
        "   python examples/server.py",
        "",
        "5. Run tests:",
        "   pytest tests/ -v",
        "",
        "6. Read documentation:",
        "   README.md for detailed information",
    ]
    
    for step in steps:
        print(step)


def main():
    """Run all tests."""
    print("\n🌍 MULTILINGUAL TRANSLATION SYSTEM - SETUP VERIFICATION")
    
    all_passed = True
    
    # Run tests
    if not test_installation():
        all_passed = False
    
    if not test_imports():
        all_passed = False
    
    if not check_project_structure():
        all_passed = False
    
    if not test_language_registry():
        all_passed = False
    
    if not test_utilities():
        all_passed = False
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60 + "\n")
    
    if all_passed:
        print("✓ ALL TESTS PASSED! ✓")
        print("\nYour multilingual translation system is ready to use!")
        show_next_steps()
    else:
        print("❌ SOME TESTS FAILED")
        print("\nPlease review the errors above and:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Check project structure and files")
        print("3. Review error messages for specific issues")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
