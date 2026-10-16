
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Illustrative examples only — not real Cynbit customer data.
TRAINING_DATA = [
    ("I need a website for my online store", "Web Development"),
    ("Build an ecommerce website for my business", "Web Development"),
    ("Create a business website with a shopping cart", "Web Development"),
    ("Develop a website for our company", "Web Development"),
    ("Create a mobile application for Android", "Mobile App Development"),
    ("I want an iOS and Android app", "Mobile App Development"),
    ("Build a mobile app for our customers", "Mobile App Development"),
    ("Develop an application for smartphones", "Mobile App Development"),
    ("Automate repetitive business tasks using AI", "AI Automation"),
    ("We need an AI chatbot for customer support", "AI Automation"),
    ("Create an intelligent assistant for our company", "AI Automation"),
    ("Use machine learning to automate our workflow", "AI Automation"),
    ("Develop a cloud-based software platform", "Cloud and SaaS"),
    ("We need a SaaS application for our customers", "Cloud and SaaS"),
    ("Deploy our application on cloud infrastructure", "Cloud and SaaS"),
    ("Build a scalable cloud software service", "Cloud and SaaS"),
]

def train_model():
    """Train a basic service-category text classifier."""
    texts = [item[0] for item in TRAINING_DATA]
    labels = [item[1] for item in TRAINING_DATA]

    classifier = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("model", LogisticRegression(max_iter=1000)),
    ])

    classifier.fit(texts, labels)
    return classifier


def detect_priority(message):
    """Apply transparent keyword rules to estimate lead priority."""
    text = message.lower()

    high_words = [
        "urgent", "urgently", "asap", "immediately",
        "deadline", "this week", "today", "tomorrow",
        "product launch", "within 7 days"
    ]

    medium_words = [
        "soon", "next month", "next week",
        "looking to start", "in a few weeks"
    ]

    high_matches = [word for word in high_words if word in text]
    medium_matches = [word for word in medium_words if word in text]

    if high_matches:
        return {
            "priority": "High",
            "reason": "Urgency or a near-term deadline was mentioned: "
                      + ", ".join(high_matches),
        }

    if medium_matches:
        return {
            "priority": "Medium",
            "reason": "The inquiry suggests a planned near-term start: "
                      + ", ".join(medium_matches),
        }

    return {
        "priority": "Low",
        "reason": "No explicit urgency or near-term deadline was detected.",
    }


def analyze_inquiry(message, classifier=None):
    """Analyze service category and estimated lead priority."""
    if not message or not message.strip():
        raise ValueError("Please enter a customer inquiry.")

    message = message.strip()

    if classifier is None:
        classifier = train_model()

    category = classifier.predict([message])[0]
    probabilities = classifier.predict_proba([message])[0]

    priority_result = detect_priority(message)

    return {
        "message": message,
        "category": str(category),
        "confidence": float(max(probabilities)),
        "priority": priority_result["priority"],
        "priority_reason": priority_result["reason"],
    }
