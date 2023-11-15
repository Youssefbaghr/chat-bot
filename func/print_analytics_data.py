
def print_analytics_data(analytics_data):
    if analytics_data:
        print("Analytics Data:")
        for index, data_point in enumerate(analytics_data, start=1):
            print(f"Data Point {index}:")
            for key, value in data_point.items():
                print(f"{key}: {value}")
            print("-" * 30)
    else:
        print("No analytics data available.")