# 🎶 NML Music Analyzer

AI destekli Türkçe şarkı sözlerinden duygu analizi yapan bir Python projesidir. Genius API üzerinden şarkı sözlerini çeker ve Hugging Face modeliyle duygu dağılımını pie chart olarak gösterir.

An AI-powered emotion analyzer for Turkish songs. It fetches lyrics from Genius API and uses a Hugging Face model to visualize emotion distribution via a pie chart.

---

## 🚀 Özellikler / Features

- 🎤 Genius.com'dan şarkı sözü çekme
- 🌐 Türkçe sözleri İngilizceye çevirme
- 🤖 Hugging Face `emotion-english-distilroberta-base` ile duygu analizi
- 📊 Matplotlib ile pasta grafik gösterimi

---

## 🧠 Kullanılan Teknolojiler / Tech Stack

- Python 3.8+
- Transformers (Hugging Face)
- Deep Translator (Google Translate)
- Requests & BeautifulSoup (lyrics çekimi)
- Matplotlib (grafik çizimi)
- FastAPI (opsiyonel REST API)

---

## 📥 Kurulum / Installation

### 1. Gerekli kütüphaneleri yükleyin:
```bash
pip install transformers torch deep-translator requests beautifulsoup4 matplotlib fastapi uvicorn
```

### 2. Genius API Token'ınızı alın:
- [Genius Developer Portal](https://genius.com/api-clients) üzerinden bir uygulama oluşturun
- `Client Access Token` kısmını kopyalayın
- `lyrics_fetcher.py` içindeki şu satırı kendi token'ınızla değiştirin:

```python
GENIUS_API_TOKEN = "Bearer SİZİN_TOKENINIZ"
```

---

## 🧪 Çalıştırma / Run Locally

### 🎧 CLI Arayüzü (Komut Satırı):

```bash
python main.py
```

Örnek giriş:
```
Şarkı Adı: Tarkan Kuzu Kuzu
```

> Şarkı sözleri çekilecek, duygu analizi yapılacak ve pie chart ile gösterilecektir.

---

### 🌐 (Opsiyonel) FastAPI sunucusu olarak çalıştır:

```bash
uvicorn main:app --reload --port 8000
```

Daha sonra bir frontend (React gibi) bu endpoint'e istek atabilir:

- `POST http://localhost:8000/analyze`
- Body:
```json
{
  "song": "Tarkan Kuzu Kuzu"
}
```

---

## 📁 Dosya Yapısı / Project Structure

```
nmlMusicAnalyzer/
│
├── main.py                    # CLI ve/veya FastAPI server
├── lyrics_fetcher.py          # Genius API'den şarkı sözleri alma
├── sentiment_analysis.py      # Çeviri + duygu analizi
├── visualize.py               # Pie chart çizimi
├── requirements.txt           # (İsteğe bağlı) kütüphane listesi
└── README.md
```

---

## 📌 Notlar / Notes

- Genius bazen bazı şarkı sözlerini çekmeyi engelleyebilir.
- Model İngilizce eğitildiği için önce otomatik çeviri yapılır.
- Kendi modelini entegre etmek istersen `sentiment_analysis.py` dosyasını düzenleyebilirsin.

---

## 👨‍💻 Geliştirici / Developer

**Muhammed Namlı**  
[https://muhammednamli.com](https://muhammednamli.com)

---

## 🪪 Lisans / License

MIT © 2025 Muhammed Namlı
