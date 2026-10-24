from fastapi import FastAPI
from pydantic import BaseModel
from src.detector import DeepfakeAndFakeNewsDetector

app = FastAPI(title="Fake News & Deepfake Voice Detector API", version="1.0")
detector = DeepfakeAndFakeNewsDetector()

class MediaInput(BaseModel):
    content_text: str
    spectral_flatness: float
    pitch_jitter: float
    energy_variance: float

@app.get("/")
def home():
    return {"message": "Fake News & Deepfake Voice Detection API is online!"}

@app.post("/verify")
def verify_media(data: MediaInput):
    txt_label, _ = detector.analyze_text_credibility(data.content_text)
    aud_label, aud_score = detector.analyze_audio_deepfake(
        data.spectral_flatness, data.pitch_jitter, data.energy_variance
    )
    is_flagged = "Fake" in txt_label or "Synthetic" in aud_label
    
    return {
        "text_analysis": txt_label,
        "audio_deepfake_analysis": aud_label,
        "artifact_score": aud_score,
        "action_required": "Quarantine / Flag Content" if is_flagged else "Approve Content"
    }
