"""Config module.

Contains supported languages and text lenght constraints.
"""

from enum import StrEnum, auto


class SupportedLanguage(StrEnum):
    """Supported languages."""

    en = auto()
    cs = auto()
    auto = auto()


# Text to translate limits
TEXT_MAX_LENGTH = 2000
TEXT_MIN_LENGTH = 1
