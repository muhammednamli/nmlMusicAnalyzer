import matplotlib.pyplot as plt

def plot_sentiment_pie(sentiment_scores, title="Duygu Analizi"):
    labels = list(sentiment_scores.keys())
    sizes = list(sentiment_scores.values())

    color_map = {
        "Mutluluk": "#f1c40f",
        "Aşk": "#e91e63",
        "Şaşkınlık": "#e67e22",
        "Öfke": "#e74c3c",
        "Üzüntü": "#3498db",
        "Korku": "#9b59b6",
        "Nötr": "#95a5a6"
    }

    colors = [color_map.get(label, "#bdc3c7") for label in labels]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    plt.title(title)
    plt.show()
