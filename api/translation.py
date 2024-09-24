"""Translation module."""
from typing import Callable

from abc import ABC, abstractmethod

from api.schemas import Translation

# Varianta 1

class Translator(ABC):
    """Base translator class."""

    @abstractmethod
    def translate(self, translation: Translation) -> Translation:
        """Translate."""
        pass


class MockTranslator(Translator):
    """Mock translator."""

    @staticmethod
    def _reverse_text(text: str) -> str:
        """Mock translate method. Just take the text and revert it."""
        return text[::-1]

    def translate(self, translation: Translation) -> Translation:
        """Translate."""
        # Do not translate if the origin and target languages are the same.
        if translation.origin_language_code == translation.target_language_code:
            return translation

        translation.text = self._reverse_text(translation.text)
        return translation


class APITranslator(Translator):
    """Google translator."""

    def translate(self, translation: Translation) -> Translation:
        """Translate using Google translator."""
        raise NotImplementedError("Google API translation is not yet implemented.")


# # Varianta 2

# TranslatorFn = Callable[[Translation], Translation] # V endpointu toto použít jako signature pro DI

# def mega_translator(translation: Translation) -> Translation:
#     translation.text = "Mega."
#     return translation

