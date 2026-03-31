import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib
matplotlib.use('TkAgg')   # Fix Tkinter issue
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Function for sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))
    
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
data['Sentiment'] = data['text'].apply(get_sentiment)

# Count values
counts = data['Sentiment'].value_counts()
print(counts)

# Plot graph
counts.plot(kind='bar')
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

# Show graph properly (fix error)
plt.show(block=True)