# Fake News and Deepfake Voice Detector

A dual-pipeline verification framework that evaluates text credibility (checking for sensationalism and false claims) while simultaneously analyzing audio waveforms and spectral features (vocoder artifacts, abnormal jitter, and flatness) to flag synthetic or AI-generated media.

## Features
- **Linguistic Credibility Analyzer:** Evaluates text bodies for misinformation markers.
- **Acoustic Spoofing Detector:** Analyzes spectral properties to spot voice cloning and vocoder artifacts.
- **FastAPI REST Endpoint:** Ready for real-time moderation pipelines.

## Project Structure
```text
fake_news_deepfake_detector/
├── data/
│   └── media_samples.csv
├── src/
│   ├── detector.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run batch evaluation script: `python src/detector.py`
3. Start API server: `uvicorn src.app:app --reload`
