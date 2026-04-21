"""
Model loading and management for multilingual translation.
"""

from typing import Dict, Optional, Tuple
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import logging

logger = logging.getLogger(__name__)


class ModelManager:
    """Manages loading and caching of translation models."""
    
    def __init__(self, device: Optional[str] = None, cache_dir: Optional[str] = None):
        """
        Initialize the model manager.
        
        Args:
            device: Device to use ('cpu', 'cuda', 'mps'). Defaults to auto-detection.
            cache_dir: Directory to cache downloaded models.
        """
        self.device = device or self._detect_device()
        self.cache_dir = cache_dir
        self.models_cache: Dict[str, Tuple] = {}
        logger.info(f"ModelManager initialized with device: {self.device}")
    
    @staticmethod
    def _detect_device() -> str:
        """Detect the best available device."""
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        return "cpu"
    
    def load_model(self, model_name: str) -> Tuple[AutoModelForSeq2SeqLM, AutoTokenizer]:
        """
        Load a MarianMT model and tokenizer.
        
        Args:
            model_name: Hugging Face model identifier (e.g., 'Helsinki-NLP/opus-mt-en-fr')
        
        Returns:
            Tuple of (model, tokenizer)
        """
        if model_name in self.models_cache:
            logger.debug(f"Loading {model_name} from cache")
            return self.models_cache[model_name]
        
        logger.info(f"Loading model: {model_name}")
        
        try:
            tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                cache_dir=self.cache_dir
            )
            model = AutoModelForSeq2SeqLM.from_pretrained(
                model_name,
                cache_dir=self.cache_dir
            )
            model = model.to(self.device)
            model.eval()
            
            self.models_cache[model_name] = (model, tokenizer)
            logger.info(f"Successfully loaded {model_name}")
            return model, tokenizer
        
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {str(e)}")
            raise
    
    def clear_cache(self) -> None:
        """Clear the model cache to free memory."""
        self.models_cache.clear()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        logger.info("Model cache cleared")
    
    def get_cached_models(self) -> list:
        """Get list of currently cached models."""
        return list(self.models_cache.keys())


class LanguagePairRegistry:
    """Registry of supported language pairs and their models."""
    
    # Common language pair models from Helsinki-NLP/opus-mt
    SUPPORTED_PAIRS = {
        ('en', 'fr'): './local_models/en-fr',
        ('en', 'de'): 'Helsinki-NLP/opus-mt-en-de',
        ('en', 'es'): 'Helsinki-NLP/opus-mt-en-es',
        ('en', 'it'): 'Helsinki-NLP/opus-mt-en-it',
        ('en', 'pt'): 'Helsinki-NLP/opus-mt-en-pt',
        ('en', 'ru'): 'Helsinki-NLP/opus-mt-en-ru',
        ('en', 'ja'): 'Helsinki-NLP/opus-mt-en-ja',
        ('en', 'zh'): 'Helsinki-NLP/opus-mt-en-zh',
        ('fr', 'en'): 'Helsinki-NLP/opus-mt-fr-en',
        ('de', 'en'): 'Helsinki-NLP/opus-mt-de-en',
        ('es', 'en'): 'Helsinki-NLP/opus-mt-es-en',
        ('it', 'en'): 'Helsinki-NLP/opus-mt-it-en',
        ('pt', 'en'): 'Helsinki-NLP/opus-mt-pt-en',
        ('ru', 'en'): 'Helsinki-NLP/opus-mt-ru-en',
        ('ja', 'en'): 'Helsinki-NLP/opus-mt-ja-en',
        ('zh', 'en'): 'Helsinki-NLP/opus-mt-zh-en',
        ('fr', 'de'): 'Helsinki-NLP/opus-mt-fr-de',
        ('de', 'fr'): 'Helsinki-NLP/opus-mt-de-fr',
        ('es', 'fr'): 'Helsinki-NLP/opus-mt-es-fr',
        ('fr', 'es'): 'Helsinki-NLP/opus-mt-fr-es',
    }
    
    @classmethod
    def get_model_name(cls, source_lang: str, target_lang: str) -> Optional[str]:
        """Get model name for a language pair."""
        return cls.SUPPORTED_PAIRS.get((source_lang.lower(), target_lang.lower()))
    
    @classmethod
    def is_supported(cls, source_lang: str, target_lang: str) -> bool:
        """Check if a language pair is supported."""
        return (source_lang.lower(), target_lang.lower()) in cls.SUPPORTED_PAIRS
    
    @classmethod
    def list_supported_pairs(cls) -> list:
        """List all supported language pairs."""
        return list(cls.SUPPORTED_PAIRS.keys())
