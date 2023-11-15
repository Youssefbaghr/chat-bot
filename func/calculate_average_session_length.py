
# Function to calculate average session length
def calculate_average_session_length(conversation_data):
    if not conversation_data:
        return 0

    timestamps = [conv['timestamp'] for conv in conversation_data]
    time_diffs = [(timestamps[i + 1] - timestamps[i]).seconds for i in range(len(timestamps) - 1)]
    avg_session_length = sum(time_diffs) / len(time_diffs) if len(time_diffs) > 0 else 0
    return avg_session_length