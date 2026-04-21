"""
Package initialization for the translation system.
"""

from .translator import MultilingualTranslator
from .models import ModelManager, LanguagePairRegistry
from .utils import (
    preprocess_text,
    split_into_sentences,
    batch_texts,
    validate_language_code,
    PerformanceMetrics,
)

__version__ = "1.0.0"
__author__ = "Translation Team"

__all__ = [
    "MultilingualTranslator",
    "ModelManager",
    "LanguagePairRegistry",
    "preprocess_text",
    "split_into_sentences",
    "batch_texts",
    "validate_language_code",
    "PerformanceMetrics",
]
