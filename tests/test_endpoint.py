"""Testing the endpoint."""

import json

import pytest
from api.config import SupportedLanguage
from api.main import app
from api.schemas import Translation
from api.translation import MockTranslator
from fastapi.testclient import TestClient

TRANSLATE_ENDPOINT = "/translate"


@pytest.fixture
def setup_client():
    app.dependency_overrides[MockTranslator] = MockTranslator
    return TestClient(app)


def test_valid_translation_endpoint(setup_client):
    translation = Translation(
        text="ABCD",
        origin_language_code=SupportedLanguage.cs,
        target_language_code=SupportedLanguage.cs,
    )

    response = setup_client.post(TRANSLATE_ENDPOINT, json=translation.model_dump())

    assert response.json() == translation.model_dump()


def test_invalid_body_missing_target_language(setup_client):
    body = {"text": "test", "origin_language": "en"}

    response = setup_client.post(TRANSLATE_ENDPOINT, json=json.dumps(body))

    assert response.status_code == 422
