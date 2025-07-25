from transformers import AutoTokenizer, AutoModelForSequenceClassification
from deep_translator import GoogleTranslator
import torch
import re

# İngilizce model
tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# Etiket eşleştirme
label_map = {
    "joy": "Mutluluk",
    "anger": "Öfke",
    "sadness": "Üzüntü",
    "fear": "Korku",
    "surprise": "Şaşkınlık",
    "love": "Aşk",
    "neutral": "Nötr"
}

def split_text(text, max_length=400):
    parts = re.split(r'[.\n\r\-]', text)
    return [p.strip() for p in parts if len(p.strip()) > 10]

def translate_to_english(text):
    return GoogleTranslator(source="auto", target="en").translate(text)

def analyze_emotions(text):
    # 1. Türkçeyi İngilizceye çevir
    translated_text = translate_to_english(text)
    
    # 2. Parçalara ayır
    parts = split_text(translated_text)
    scores = {label: 0 for label in label_map.keys()}

    for part in parts:
        inputs = tokenizer(part, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        for i, label in enumerate(label_map.keys()):
            scores[label] += float(probs[0][i])

    # 3. Normalize
    total = sum(scores.values())
    averaged_scores = {label_map[label]: round(scores[label] / total, 4) for label in label_map}
    return averaged_scores
