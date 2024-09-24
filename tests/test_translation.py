import pytest
from api.config import SupportedLanguage
from api.schemas import Translation
from api.translation import MockTranslator


@pytest.fixture
def mock_translator():
    """Fixture for creating a MockTranslator instance."""
    return MockTranslator()


def test_mock_translate_reverses_text(mock_translator):
    """Test that text is reversed when translating between different languages."""
    translation = Translation(
        text="hello",
        origin_language_code=SupportedLanguage.en,
        target_language_code=SupportedLanguage.cs,
    )
    result = mock_translator.translate(translation)
    assert result.text == "olleh"


def test_mock_no_translation_same_language(mock_translator):
    """Test that text remains the same when origin and target languages are the same."""
    translation = Translation(
        text="hello",
        origin_language_code=SupportedLanguage.en,
        target_language_code=SupportedLanguage.en,
    )
    result = mock_translator.translate(translation)
    assert result.text == "hello"
