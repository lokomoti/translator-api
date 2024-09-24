import random

import pytest
from pydantic import ValidationError

from api import config
from api.config import SupportedLanguage
from api.schemas import Translation


def test_translation_valid_data():
    """Test valid data."""

    translation_text = "Test translation text."
    origin_language = random.choice(list(SupportedLanguage))
    target_language = random.choice(list(SupportedLanguage))

    translation = Translation(
        text=translation_text,
        origin_language_code=origin_language,
        target_language_code=target_language,
    )

    assert translation.text == translation_text
    assert translation.origin_language_code.value == origin_language
    assert translation.target_language_code.value == target_language


def test_translation_invalid_text_too_short():
    data = {
        "text": "",
        "origin_language_code": SupportedLanguage.en,
        "target_language_code": SupportedLanguage.cs,
    }
    with pytest.raises(ValidationError):
        Translation(**data)


def test_translation_invalid_text_none():
    data = {
        "text": None,
        "origin_language_code": SupportedLanguage.en,
        "target_language_code": SupportedLanguage.cs,
    }
    with pytest.raises(ValidationError):
        Translation(**data)


def test_translation_invalid_text_number():
    data = {
        "text": 152,
        "origin_language_code": SupportedLanguage.en,
        "target_language_code": SupportedLanguage.cs,
    }
    with pytest.raises(ValidationError):
        Translation(**data)


def test_translation_invalid_text_too_long():
    data = {
        "text": "A" * (config.TEXT_MAX_LENGTH + 1),
        "origin_language_code": config.SupportedLanguage.en,
        "target_language_code": config.SupportedLanguage.cs,
    }
    with pytest.raises(ValidationError):
        Translation(**data)


def test_translation_invalid_origin_language_code():
    data = {
        "text": "Hello, world!",
        "origin_language_code": "INVALID_CODE",  # Invalid language code
        "target_language_code": SupportedLanguage.cs,
    }
    with pytest.raises(ValidationError):
        Translation(**data)


def test_translation_invalid_target_language_code():
    data = {
        "text": "Hello, world!",
        "origin_language_code": SupportedLanguage.en,
        "target_language_code": "INVALID_CODE",  # Invalid language code
    }
    with pytest.raises(ValueError):
        Translation(**data)


def test_translation_missing_fields():
    data = {
        "text": "Hello, world!"
        # Missing origin_language_code and target_language_code
    }
    with pytest.raises(ValidationError):
        Translation(**data)
