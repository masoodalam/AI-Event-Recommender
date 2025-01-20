def recommend_events(user_data):
    preferences = user_data.get('preferences', [])
    location = user_data.get('location', '')

    # Simulated list of events
    events = [
        {"name": "Music Concert", "category": "Music", "location": "Edinburgh"},
        {"name": "Tech Meetup", "category": "Technology", "location": "Glasgow"},
        {"name": "Art Workshop", "category": "Art", "location": "Edinburgh"},
        {"name": "Food Festival", "category": "Food", "location": "Edinburgh"},
    ]

    # Filter events based on user preferences and location
    recommended = [
        event for event in events
        if event["category"] in preferences and event["location"] == location
    ]

    return {"recommended_events": recommended}
