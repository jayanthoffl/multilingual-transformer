"""
Unit tests for the translation system.
"""

import pytest
from src.translator import MultilingualTranslator
from src.models import LanguagePairRegistry
from src.utils import (
    preprocess_text,
    split_into_sentences,
    batch_texts,
    validate_language_code,
)


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_preprocess_text(self):
        """Test text preprocessing."""
        text = "Hello  world   with   spaces"
        result = preprocess_text(text)
        assert result == "Hello world with spaces"
    
    def test_preprocess_text_strip(self):
        """Test text stripping."""
        text = "   Hello world   "
        result = preprocess_text(text)
        assert result == "Hello world"
    
    def test_split_into_sentences(self):
        """Test sentence splitting."""
        text = "Hello world. How are you? I am fine!"
        result = split_into_sentences(text)
        assert len(result) == 3
    
    def test_batch_texts(self):
        """Test text batching."""
        texts = ["a", "b", "c", "d", "e"]
        result = batch_texts(texts, batch_size=2)
        assert len(result) == 3
        assert result[0] == ["a", "b"]
        assert result[1] == ["c", "d"]
        assert result[2] == ["e"]
    
    def test_validate_language_code(self):
        """Test language code validation."""
        assert validate_language_code("en") is True
        assert validate_language_code("fr") is True
        assert validate_language_code("EN") is True
        assert validate_language_code("eng") is False
        assert validate_language_code("e") is False
        assert validate_language_code("123") is False


class TestLanguagePairRegistry:
    """Test language pair registry."""
    
    def test_is_supported(self):
        """Test language pair support check."""
        assert LanguagePairRegistry.is_supported("en", "fr") is True
        assert LanguagePairRegistry.is_supported("en", "de") is True
        assert LanguagePairRegistry.is_supported("un", "kr") is False
    
    def test_get_model_name(self):
        """Test getting model name for language pair."""
        model = LanguagePairRegistry.get_model_name("en", "fr")
        assert model is not None
        assert "Helsinki-NLP" in model
    
    def test_list_supported_pairs(self):
        """Test listing supported pairs."""
        pairs = LanguagePairRegistry.list_supported_pairs()
        assert len(pairs) > 0
        assert ("en", "fr") in pairs
    
    def test_case_insensitive(self):
        """Test case-insensitive language codes."""
        assert LanguagePairRegistry.is_supported("EN", "FR") is True
        assert LanguagePairRegistry.is_supported("En", "Fr") is True


class TestMultilingualTranslator:
    """Test multilingual translator."""
    
    @pytest.fixture
    def translator(self):
        """Create translator instance."""
        return MultilingualTranslator(enable_metrics=False)
    
    def test_initialization(self, translator):
        """Test translator initialization."""
        assert translator is not None
        assert translator.device in ["cpu", "cuda", "mps"]
    
    def test_get_supported_languages(self, translator):
        """Test getting supported languages."""
        supported = translator.get_supported_languages()
        assert "en" in supported
        assert "fr" in supported.get("en", [])
    
    def test_invalid_language_pair(self, translator):
        """Test error on invalid language pair."""
        with pytest.raises(ValueError):
            translator.translate("hello", "xx", "yy")
    
    def test_invalid_language_code(self, translator):
        """Test error on invalid language code."""
        with pytest.raises(ValueError):
            translator.translate("hello", "eng", "fr")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
