from gensim import corpora, models
from func.preprocess_text import  preprocess_text

# Function to perform topic modeling
def perform_topic_modeling(conversation_data):
    texts = []

    for conversation in conversation_data:
        text = conversation.get('user_input', '') + ' ' + conversation.get('bot_response', '')
        tokens = preprocess_text(text)
        texts.append(tokens)

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    prevalent_topics = lda_model.print_topics()

    return prevalent_topics