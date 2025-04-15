
import random

def analyze_dream(text):
    # Basic mock dream interpretation logic (can later be AI-enhanced)
    emotions = ['happy', 'scary', 'confusing', 'peaceful', 'anxious']
    keywords = ['water', 'flight', 'falling', 'dark', 'light']
    interpretation = "This dream might reflect inner thoughts or emotions."

    return {
        'emotion': random.choice(emotions),
        'keywords': [word for word in keywords if word in text.lower()],
        'interpretation': interpretation
    }
