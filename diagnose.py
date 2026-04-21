"""
DIAGNOSTIC REPORT & SETUP GUIDE
================================

This script checks your setup and shows how to run the translation system.
"""

import sys
import os
from pathlib import Path

def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def check_python_version():
    """Check Python version."""
    print_section("1. PYTHON VERSION CHECK")
    version = sys.version_info
    print(f"  Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("  ✓ Python version is compatible\n")
        return True
    else:
        print("  ❌ Python 3.8+ required\n")
        return False


def check_dependencies():
    """Check required dependencies."""
    print_section("2. DEPENDENCY CHECK")
    
    required = {
        'torch': 'PyTorch',
        'transformers': 'Hugging Face Transformers',
        'sentencepiece': 'SentencePiece',
    }
    
    missing = []
    for module, name in required.items():
        try:
            __import__(module)
            print(f"  ✓ {name:40} installed")
        except ImportError:
            print(f"  ❌ {name:40} NOT installed")
            missing.append(module)
    
    if missing:
        print(f"\n  ⚠️  Missing packages: {', '.join(missing)}")
        print(f"\n  Fix with: pip install -r requirements.txt\n")
        return False
    else:
        print("\n  ✓ All required packages installed\n")
        return True


def check_project_files():
    """Check project files."""
    print_section("3. PROJECT FILE CHECK")
    
    required_files = [
        'src/__init__.py',
        'src/translator.py',
        'src/models.py',
        'src/utils.py',
        'cli.py',
        'requirements.txt',
        'README.md',
    ]
    
    missing = []
    for file_path in required_files:
        full_path = Path(file_path)
        if full_path.exists():
            print(f"  ✓ {file_path:40} found")
        else:
            print(f"  ❌ {file_path:40} MISSING")
            missing.append(file_path)
    
    if missing:
        print(f"\n  ⚠️  Missing files: {missing}\n")
        return False
    else:
        print("\n  ✓ All required files present\n")
        return True


def show_issues_found():
    """Show known issues and fixes."""
    print_section("4. KNOWN ISSUES & FIXES")
    
    issues = [
        {
            'title': 'Old interactive.py requires running server',
            'fix': 'Use the new cli.py instead which runs standalone!'
        },
        {
            'title': 'Files in root directory are from previous setup',
            'fix': 'They can be removed. Use cli.py as the main interface.'
        },
        {
            'title': 'First translation is slow (models downloading)',
            'fix': 'Normal! Models cache after first download (~500MB each)'
        },
        {
            'title': 'Need internet for first run',
            'fix': 'Models download from Hugging Face. Second run is offline OK.'
        },
    ]
    
    for i, issue in enumerate(issues, 1):
        print(f"  {i}. Issue: {issue['title']}")
        print(f"     Fix:   {issue['fix']}\n")


def show_quick_start():
    """Show quick start guide."""
    print_section("5. QUICK START GUIDE")
    
    print("  Step 1: Install dependencies (if needed)\n")
    print("    $ pip install -r requirements.txt\n")
    
    print("  Step 2: Run the interactive CLI\n")
    print("    $ python cli.py\n")
    
    print("  Step 3: Use the CLI\n")
    print("    🔷 Enter command: translate")
    print("    Enter source language code (e.g., 'en'): en")
    print("    Enter target language code (e.g., 'fr'): fr")
    print("    Enter text to translate: Hello, how are you?\n")
    
    print("  Step 4: Available commands in CLI\n")
    print("    - translate     : Interactive translation")
    print("    - quick en TEXT : Quick translation from English")
    print("    - supported     : Show supported language pairs")
    print("    - recent        : Show recent translations")
    print("    - help          : Show help")
    print("    - quit          : Exit\n")


def show_alternatives():
    """Show alternative ways to use the system."""
    print_section("6. ALTERNATIVE USAGE METHODS")
    
    print("  Method 1: Interactive CLI (RECOMMENDED)")
    print("    $ python cli.py\n")
    
    print("  Method 2: Quick translation from command line")
    print("    $ python -c \"from src.translator import MultilingualTranslator as MT; print(MT().translate('Hello', 'en', 'fr'))\"\n")
    
    print("  Method 3: Python script")
    print("    from src.translator import MultilingualTranslator")
    print("    translator = MultilingualTranslator()")
    print("    result = translator.translate('Hello', 'en', 'fr')")
    print("    print(result)\n")
    
    print("  Method 4: Flask API Server (requires separate terminal)")
    print("    Terminal 1: $ python examples/server.py")
    print("    Terminal 2: Use examples/simple_translation.py\n")


def show_features():
    """Show available features."""
    print_section("7. SUPPORTED FEATURES")
    
    print("  Language Pairs: 20+ pairs including")
    print("    - English ↔ French, German, Spanish, Italian, Portuguese")
    print("    - English ↔ Russian, Japanese, Chinese")
    print("    - French ↔ German, Spanish")
    print("    - German ↔ Spanish, Italian, Portuguese")
    print("    - And more!\n")
    
    print("  Features:")
    print("    ✓ Single text translation")
    print("    ✓ Batch translation")
    print("    ✓ Performance metrics")
    print("    ✓ Model caching")
    print("    ✓ CPU/GPU support")
    print("    ✓ Error handling\n")


def main():
    """Run diagnostic."""
    print("\n")
    print("╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  MULTILINGUAL TRANSLATOR - DIAGNOSTIC & SETUP GUIDE".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")
    
    # Run checks
    python_ok = check_python_version()
    deps_ok = check_dependencies()
    files_ok = check_project_files()
    
    # Show issues and fixes
    show_issues_found()
    show_quick_start()
    show_alternatives()
    show_features()
    
    # Summary
    print_section("8. STATUS SUMMARY")
    
    if python_ok and deps_ok and files_ok:
        print("  ✓ READY TO USE!")
        print("\n  Next step: Run 'python cli.py' to start translating!\n")
    else:
        print("  ⚠️  SETUP NEEDED")
        print("\n  Issues to fix:")
        if not python_ok:
            print("    - Update Python to 3.8+")
        if not deps_ok:
            print("    - Install missing dependencies: pip install -r requirements.txt")
        if not files_ok:
            print("    - Check project files\n")


if __name__ == "__main__":
    main()
    print("="*70 + "\n")
