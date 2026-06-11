import google.generativeai as genai

# Paste your Gemini API key here temporarily
API_KEY = "your api_key"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_remark(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze the following patient health values:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give a short health assessment and recommendations.
    """

    try:

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

    except Exception as e:

        print("AI ERROR:", e)

    # Fallback mechanism

    remarks = []

    if glucose > 180:
        remarks.append(
            "Very high glucose levels detected. Immediate medical consultation is recommended."
        )

    elif glucose > 140:
        remarks.append(
            "High glucose levels detected. Possible diabetes risk."
        )

    else:
        remarks.append(
            "Glucose levels appear to be within the normal range."
        )

    if haemoglobin < 12:
        remarks.append(
            "Low haemoglobin levels detected. Possible anemia risk."
        )

    else:
        remarks.append(
            "Haemoglobin levels appear normal."
        )

    if cholesterol > 240:
        remarks.append(
            "Very high cholesterol levels detected. Increased cardiovascular risk."
        )

    elif cholesterol > 200:
        remarks.append(
            "High cholesterol levels detected. Lifestyle modifications may be required."
        )

    else:
        remarks.append(
            "Cholesterol levels appear normal."
        )

    remarks.append(
        "Please consult a healthcare professional for proper diagnosis."
    )

    return " ".join(remarks)