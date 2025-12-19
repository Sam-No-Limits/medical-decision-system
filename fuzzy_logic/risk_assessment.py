def assess_risk(ml_confidence, similarity_score):
    """
    Dummy fuzzy logic combining ML confidence and similarity
    Returns risk level as string.
    """
    score = 0.7 * ml_confidence + 0.3 * similarity_score
    if score > 0.8:
        return "Critical"
    elif score > 0.6:
        return "High"
    elif score > 0.4:
        return "Medium"
    else:
        return "Low"
