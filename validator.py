from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class SupportResponse(BaseModel):
    intent: str
    urgency: str
    response_en: str
    response_ar: str
    confidence: float = Field(ge=0.0, le=1.0)
    tool_call: Optional[Dict[str, Any]] = None