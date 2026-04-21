"""
Utility functions for the translation system.
"""

import re
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


def preprocess_text(text: str) -> str:
    """
    Preprocess text for translation.
    
    Args:
        text: Input text
    
    Returns:
        Preprocessed text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text


def split_into_sentences(text: str, max_length: int = 500) -> List[str]:
    """
    Split text into sentences and chunks.
    
    Args:
        text: Input text
        max_length: Maximum length of each chunk
    
    Returns:
        List of sentences/chunks
    """
    # Simple sentence splitting based on common punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += (" " if current_chunk else "") + sentence
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks


def batch_texts(texts: List[str], batch_size: int = 32) -> List[List[str]]:
    """
    Create batches from a list of texts.
    
    Args:
        texts: List of texts
        batch_size: Size of each batch
    
    Returns:
        List of batches
    """
    batches = []
    for i in range(0, len(texts), batch_size):
        batches.append(texts[i:i + batch_size])
    return batches


def validate_language_code(lang_code: str) -> bool:
    """
    Validate ISO 639-1 language code.
    
    Args:
        lang_code: Language code (e.g., 'en', 'fr')
    
    Returns:
        True if valid, False otherwise
    """
    # ISO 639-1 codes are 2 lowercase letters
    return bool(re.match(r'^[a-z]{2}$', lang_code.lower()))


def format_translation_result(
    original_text: str,
    translated_text: str,
    source_lang: str,
    target_lang: str,
    confidence: float = 1.0
) -> Dict:
    """
    Format translation result as a dictionary.
    
    Args:
        original_text: Original text
        translated_text: Translated text
        source_lang: Source language code
        target_lang: Target language code
        confidence: Confidence score
    
    Returns:
        Formatted result dictionary
    """
    return {
        "original": original_text,
        "translation": translated_text,
        "source_language": source_lang,
        "target_language": target_lang,
        "confidence": confidence,
    }


def merge_translations(translations: List[str], original_separator: str = " ") -> str:
    """
    Merge translated sentences back into a single text.
    
    Args:
        translations: List of translated sentences
        original_separator: Separator between sentences
    
    Returns:
        Merged translation
    """
    return original_separator.join(translations)


class PerformanceMetrics:
    """Track performance metrics for translation."""
    
    def __init__(self):
        self.translation_times = []
        self.batch_sizes = []
        self.tokens_processed = 0
    
    def add_measurement(self, time_ms: float, tokens: int, batch_size: int = 1):
        """Record a translation measurement."""
        self.translation_times.append(time_ms)
        self.batch_sizes.append(batch_size)
        self.tokens_processed += tokens
    
    def get_stats(self) -> Dict:
        """Get performance statistics."""
        if not self.translation_times:
            return {
                "avg_time_ms": 0,
                "total_time_ms": 0,
                "total_tokens": 0,
                "translation_count": 0,
            }
        
        return {
            "avg_time_ms": sum(self.translation_times) / len(self.translation_times),
            "total_time_ms": sum(self.translation_times),
            "total_tokens": self.tokens_processed,
            "translation_count": len(self.translation_times),
            "tokens_per_sec": (self.tokens_processed * 1000) / sum(self.translation_times)
                              if sum(self.translation_times) > 0 else 0,
        }
    
    def reset(self):
        """Reset metrics."""
        self.translation_times = []
        self.batch_sizes = []
        self.tokens_processed = 0
