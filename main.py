from fastapi import Depends, FastAPI, status, HTTPException

from api import translation
from api.exceptions import TranslatorError
from api.schemas import Translation
from api.translation import Translator

app = FastAPI()


@app.post("/translate")
def translate(
    translation: Translation,
    translator: Translator = Depends(translation.get_translator),
):
    """Translation endpoint."""

    try:
        return translator.translate(translation)

    except TranslatorError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Translation failed: {str(e)}"
        )
    
    