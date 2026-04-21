"""
Main translator module for multilingual text translation.
Uses MarianMT models from Hugging Face Transformers.
"""

import time
from typing import List, Dict, Optional, Union
import torch
import logging
from .models import ModelManager, LanguagePairRegistry
from .utils import (
    preprocess_text,
    split_into_sentences,
    batch_texts,
    validate_language_code,
    format_translation_result,
    merge_translations,
    PerformanceMetrics,
)

logger = logging.getLogger(__name__)


class MultilingualTranslator:
    """
    Main translator class for translating text between multiple languages.
    Supports batch processing and multiple language pairs.
    """
    
    def __init__(
        self,
        device: Optional[str] = None,
        cache_dir: Optional[str] = None,
        enable_metrics: bool = False,
    ):
        """
        Initialize the translator.
        
        Args:
            device: Device to use ('cpu', 'cuda', 'mps')
            cache_dir: Directory to cache models
            enable_metrics: Enable performance tracking
        """
        self.model_manager = ModelManager(device=device, cache_dir=cache_dir)
        self.device = self.model_manager.device
        self.enable_metrics = enable_metrics
        self.metrics = PerformanceMetrics() if enable_metrics else None
        logger.info(f"MultilingualTranslator initialized on {self.device}")
    
    def translate(
        self,
        text: str,
        source_lang: str,
        target_lang: str,
        batch_size: int = 32,
        return_full_result: bool = False,
    ) -> Union[str, Dict]:
        """
        Translate text from one language to another.
        
        Args:
            text: Text to translate
            source_lang: Source language code (e.g., 'en')
            target_lang: Target language code (e.g., 'fr')
            batch_size: Batch size for processing
            return_full_result: Return full result dict or just translation
        
        Returns:
            Translated text or full result dictionary
        
        Raises:
            ValueError: If language pair is not supported
        """
        # Validate inputs
        if not validate_language_code(source_lang):
            raise ValueError(f"Invalid source language code: {source_lang}")
        if not validate_language_code(target_lang):
            raise ValueError(f"Invalid target language code: {target_lang}")
        
        if not LanguagePairRegistry.is_supported(source_lang, target_lang):
            raise ValueError(
                f"Unsupported language pair: {source_lang} -> {target_lang}"
            )
        
        # Preprocess and split text
        text = preprocess_text(text)
        sentences = split_into_sentences(text)
        
        # Translate
        start_time = time.time()
        translated_sentences = self._translate_batch(
            sentences, source_lang, target_lang, batch_size
        )
        elapsed_time = time.time() - start_time
        
        # Merge results
        translated_text = merge_translations(translated_sentences)
        
        # Track metrics
        if self.enable_metrics:
            tokens = sum(len(s.split()) for s in sentences)
            self.metrics.add_measurement(elapsed_time * 1000, tokens, len(sentences))
        
        logger.info(
            f"Translated {len(sentences)} sentences in {elapsed_time:.2f}s"
        )
        
        if return_full_result:
            return format_translation_result(
                text, translated_text, source_lang, target_lang
            )
        
        return translated_text
    
    def translate_batch(
        self,
        texts: List[str],
        source_lang: str,
        target_lang: str,
        batch_size: int = 32,
    ) -> List[str]:
        """
        Translate multiple texts.
        
        Args:
            texts: List of texts to translate
            source_lang: Source language code
            target_lang: Target language code
            batch_size: Batch size for processing
        
        Returns:
            List of translated texts
        """
        if not LanguagePairRegistry.is_supported(source_lang, target_lang):
            raise ValueError(
                f"Unsupported language pair: {source_lang} -> {target_lang}"
            )
        
        # Preprocess all texts
        texts = [preprocess_text(t) for t in texts]
        
        # Translate
        start_time = time.time()
        translated = self._translate_batch(texts, source_lang, target_lang, batch_size)
        elapsed_time = time.time() - start_time
        
        logger.info(
            f"Translated {len(texts)} texts in {elapsed_time:.2f}s"
        )
        
        return translated
    
    def _translate_batch(
        self,
        texts: List[str],
        source_lang: str,
        target_lang: str,
        batch_size: int,
    ) -> List[str]:
        """
        Internal method to translate a batch of texts.
        
        Args:
            texts: List of texts to translate
            source_lang: Source language code
            target_lang: Target language code
            batch_size: Batch size for processing
        
        Returns:
            List of translated texts
        """
        # Load model
        model_name = LanguagePairRegistry.get_model_name(source_lang, target_lang)
        model, tokenizer = self.model_manager.load_model(model_name)
        
        # Prepare prefix for MarianMT models
        prefix = f">>{target_lang.upper()}<< "
        texts_with_prefix = [prefix + text for text in texts]
        
        # Batch and translate
        batches = batch_texts(texts_with_prefix, batch_size)
        translations = []
        
        with torch.no_grad():
            for batch in batches:
                # Tokenize
                inputs = tokenizer(
                    batch,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=512,
                )
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                
                # Generate translations
                outputs = model.generate(
                    **inputs,
                    max_length=512,
                    num_beams=4,
                    early_stopping=True,
                )
                
                # Decode
                batch_translations = tokenizer.batch_decode(
                    outputs, skip_special_tokens=True
                )
                translations.extend(batch_translations)
        
        return translations
    
    def get_supported_languages(self) -> Dict[str, List[str]]:
        """
        Get supported language pairs.
        
        Returns:
            Dictionary mapping from languages to supported target languages
        """
        supported_pairs = LanguagePairRegistry.list_supported_pairs()
        result = {}
        
        for source, target in supported_pairs:
            if source not in result:
                result[source] = []
            result[source].append(target)
        
        return result
    
    def get_metrics(self) -> Optional[Dict]:
        """Get performance metrics if enabled."""
        if self.enable_metrics:
            return self.metrics.get_stats()
        return None
    
    def clear_cache(self) -> None:
        """Clear model cache to free memory."""
        self.model_manager.clear_cache()
        logger.info("Cache cleared")
    
    def detect_language(self, text: str) -> Optional[str]:
        """
        Detect the language of input text.
        Note: This is a placeholder that could integrate with langdetect.
        
        Args:
            text: Text to detect
        
        Returns:
            Language code or None
        """
        # TODO: Implement language detection with langdetect
        logger.warning("Language detection not implemented")
        return None
