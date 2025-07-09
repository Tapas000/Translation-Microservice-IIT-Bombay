from pydantic import BaseModel, Field,constr
from typing import List, Optional

class BulkTranslationRequest(BaseModel):
    texts: List[str]
    target_lang: str

class TranslationResponse(BaseModel):
    translated_text: str

class HealthCheckResponse(BaseModel):
    status: str

class TranslationRequest(BaseModel):
    text: constr(max_length=10000)
    target_lang: str
