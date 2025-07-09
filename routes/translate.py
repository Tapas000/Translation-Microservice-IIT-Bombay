from fastapi import APIRouter, HTTPException
from models.schemas import *
from services.translator import translate_text
from utils.logger import log_translation

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
def translate(req: TranslationRequest):
    try:
        translated = translate_text(req.text, req.target_lang)
        log_translation(req.text, req.target_lang, translated)
        return {"translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health", response_model=HealthCheckResponse)
def health_check():
    return {"status": "ok"}
