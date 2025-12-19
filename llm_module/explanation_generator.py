def generate_explanation(disease, confidence, risk_level):
    """
    Dummy LLM explanation generator
    """
    explanation = f"Predicted disease: {disease}, confidence: {confidence:.2f}, risk level: {risk_level}."
    recommendation = "Consult doctor for next steps."
    return {"explanation": explanation, "recommendation": recommendation}
