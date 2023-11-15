from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Initialize NLTK components outside functions for optimization
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Combine preprocess_text and calculate_similarity functions
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words and word not in string.punctuation
    ]
    return cleaned_tokens
