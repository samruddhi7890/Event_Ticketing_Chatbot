from app.groq_client import call_groq


def compress_event_catalog(events):

    prompt = f"""
    Compress the following event catalog by 80% while preserving key information:
    {events}
    """

    response = call_groq(prompt)
    return response["choices"][0]["message"]["content"]


def recommend_events(user_interest, events):

    interest_lower = user_interest.lower()

    # 🌍 Vast Keyword Mapping
    category_keywords = {
        "music": [
            "concert", "music", "gig", "dj", "festival",
            "band", "live"
        ],

        "comedy": [
            "comedy", "stand-up", "funny", "humor",
            "laugh", "comic"
        ],

        "technology": [
            "tech", "technology", "ai", "machine learning",
            "data", "cyber", "blockchain", "startup",
            "conference"
        ],

        "business": [
            "business", "networking", "entrepreneur",
            "seminar", "leadership", "marketing"
        ],

        "education": [
            "workshop", "training", "course",
            "bootcamp", "learning", "class"
        ],

        "sports": [
            "sports", "match", "cricket", "football",
            "tournament", "game"
        ]
    }

    filtered_events = []

    # 🎯 Step 1: Detect interest category
    detected_keywords = []

    for category, keywords in category_keywords.items():
        if any(keyword in interest_lower for keyword in keywords):
            detected_keywords = keywords
            break

    # 🎯 Step 2: Flexible matching
    if detected_keywords:
        filtered_events = [
            event for event in events
            if any(keyword in event["name"].lower() for keyword in detected_keywords)
        ]

    # ✅ Step 3: Fallback if empty
    if not filtered_events:
        filtered_events = events

    prompt = f"""
    User interest: {user_interest}

    Events:
    {filtered_events}

    Recommend the best matches with a short explanation.
    """

    response = call_groq(prompt)
    return response["choices"][0]["message"]["content"]
