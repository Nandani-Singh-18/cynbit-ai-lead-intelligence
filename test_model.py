
from model import analyze_inquiry, detect_priority


def test_web_development_category():
    result = analyze_inquiry(
        "I need an ecommerce website for my business"
    )
    assert result["category"] == "Web Development"


def test_ai_automation_category():
    result = analyze_inquiry(
        "We need an AI chatbot for customer support"
    )
    assert result["category"] == "AI Automation"


def test_high_priority():
    result = detect_priority(
        "We urgently need a solution before our product launch"
    )
    assert result["priority"] == "High"


def test_medium_priority():
    result = detect_priority(
        "We are looking to start next month"
    )
    assert result["priority"] == "Medium"


def test_low_priority():
    result = detect_priority(
        "We are exploring software options for our business"
    )
    assert result["priority"] == "Low"


def test_empty_inquiry():
    try:
        analyze_inquiry("")
        assert False, "Expected ValueError for an empty inquiry"
    except ValueError:
        pass
