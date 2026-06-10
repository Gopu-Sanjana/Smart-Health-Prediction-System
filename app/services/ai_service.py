def generate_ai_remark(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give a short health assessment.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        return (
            "AI service temporarily unavailable. "
            "Patient values should be reviewed by a healthcare professional."
        )