from func.calculate_average_session_length import calculate_average_session_length

# Function to calculate user engagement metrics
def calculate_user_engagement(conversation_data):
    engagement_metrics = {
        'average_session_length': calculate_average_session_length(conversation_data),
    }
    return engagement_metrics
