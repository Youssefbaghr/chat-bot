# Function to calculate Jaccard similarity
def calculate_similarity(tokens1, tokens2):
    intersection = len(set(tokens1).intersection(tokens2))
    union = len(set(tokens1).union(tokens2))
    similarity = intersection / union if union > 0 else 0
    return similarity