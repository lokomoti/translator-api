"""Testing the endpoint."""

import pytest
from fastapi.testclient import TestClient

from api.config import SupportedLanguage
from api.main import app
from api.schemas import Translation
from api.translation import MockTranslator


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

    response = setup_client.post("/translate", json=translation.model_dump())

    assert response.json() == translation.model_dump()
