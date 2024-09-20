"""Schemas module."""

from pydantic import BaseModel, Field

import api.config as config


class Translation(BaseModel):
    """Translation model for request and response."""

    text: str = Field(
        max_length=config.TEXT_MAX_LENGTH, min_length=config.TEXT_MIN_LENGTH
    )
    origin_language_code: config.SupportedLanguage
    target_language_code: config.SupportedLanguage
