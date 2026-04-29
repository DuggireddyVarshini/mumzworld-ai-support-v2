def compute_confidence(intent_score, faq_score=None):
    base = intent_score

    if faq_score:
        base = (intent_score + faq_score) / 2
        base = min(base, 0.95)

    return round(max(base, 0.15), 2)