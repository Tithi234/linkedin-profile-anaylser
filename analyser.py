def analyze_profile(headline, about):

    keywords = [
        "python",
        "data",
        "machine learning",
        "ai",
        "analytics",
        "developer",
        "student",
        "engineer"
    ]

    found_keywords = []

    text = (headline + " " + about).lower()

    for word in keywords:
        if word in text:
            found_keywords.append(word)

    score = 50

    if len(headline) > 40:
        score += 10

    if len(about) > 200:
        score += 20

    score += len(found_keywords) * 3

    suggestions = []

    if len(headline) < 40:
        suggestions.append("Make your headline more descriptive.")

    if len(about) < 200:
        suggestions.append("Write a longer about section.")

    if len(found_keywords) < 3:
        suggestions.append("Add more industry keywords.")

    if "python" not in text:
        suggestions.append("Mention your technical skills like Python.")

    if "data" not in text:
        suggestions.append("Highlight data-related skills.")

    return {
        "score": min(score, 100),
        "headline_length": len(headline),
        "about_length": len(about),
        "keywords": found_keywords,
        "suggestions": suggestions
    }
