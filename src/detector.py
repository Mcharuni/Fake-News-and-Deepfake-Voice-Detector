import pandas as pd
import numpy as np

class DeepfakeAndFakeNewsDetector:
    def __init__(self, data_path="data/media_samples.csv"):
        self.df = pd.read_csv(data_path)

    def analyze_text_credibility(self, text):
        sensational_keywords = ["breaking", "secret", "shocking", "hiding", "leaked", "miracle"]
        score = sum(1 for word in sensational_keywords if word in text.lower())
        if score >= 2:
            return "High Fake News Risk", 0.90
        elif score == 1:
            return "Moderate Credibility Concern", 0.60
        return "Likely Authentic Text", 0.10

    def analyze_audio_deepfake(self, flatness, jitter, variance):
        # AI-generated voices often exhibit abnormal smoothness (low spectral flatness), high jitter, and low energy variance
        artifact_index = ((0.05 - flatness) / 0.05 * 0.4) + (jitter / 0.1 * 0.4) + ((0.05 - variance) / 0.05 * 0.2)
        if artifact_index > 0.65:
            return "Synthetic / Deepfake Audio Detected", round(artifact_index, 2)
        return "Authentic Human Voice", round(artifact_index, 2)

    def process_batch(self):
        results = []
        for _, row in self.df.iterrows():
            txt_label, txt_conf = self.analyze_text_credibility(row["headline_or_text"])
            aud_label, aud_score = self.analyze_audio_deepfake(
                row["spectral_flatness"], row["pitch_jitter"], row["energy_variance"]
            )
            
            risk_status = "Flagged as Malicious/Synthetic" if "Fake" in txt_label or "Deepfake" in aud_label else "Verified Clean"
            
            results.append({
                "sample_id": row["sample_id"],
                "text_credibility": txt_label,
                "audio_authenticity": aud_label,
                "synthesized_artifact_score": aud_score,
                "overall_status": risk_status
            })
        return pd.DataFrame(results)

if __name__ == "__main__":
    detector = DeepfakeAndFakeNewsDetector()
    print(detector.process_batch())
