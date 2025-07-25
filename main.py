from lyrics_fetcher import search_song_lyrics
from sentiment_analysis import analyze_emotions
from visualize import plot_sentiment_pie

if __name__ == "__main__":
    song = input("🎵 Şarkı Adı: ")
    lyrics = search_song_lyrics(song)
    
    if not lyrics or lyrics.startswith("Hata") or lyrics == "Sözler alınamadı.":
        print("❌ Şarkı sözleri alınamadı.")
    else:
        print("\n🎤 Şarkı Sözleri:\n", lyrics)

        print("\n📊 Duygu Analizi:")
        result = analyze_emotions(lyrics)

        for emotion, score in result.items():
            print(f"{emotion}: {score * 100:.2f}%")

        plot_sentiment_pie(result, title=f"{song} - Duygu Dağılımı")
