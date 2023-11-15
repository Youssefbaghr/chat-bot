from nltk.sentiment import SentimentIntensityAnalyzer

# Function to perform sentiment analysis
def perform_sentiment_analysis(conversation_data):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = []

    for conversation in conversation_data:
        text = conversation.get('user_input', '') + ' ' + conversation.get('bot_response', '')
        scores = sid.polarity_scores(text)
        sentiment_scores.append(scores)

    return sentiment_scores