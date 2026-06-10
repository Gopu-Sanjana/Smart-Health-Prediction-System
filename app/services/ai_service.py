import os
import google.generativeai as genai


API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


def generate_ai_remark(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze the following patient values:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give a short health assessment and recommendations.
    """

    # Try Gemini first
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            pass

    # Fallback logic
    remarks = []

    if glucose > 140:
        remarks.append(
            "High glucose level detected. Possible diabetes risk."
        )

    if haemoglobin < 12:
        remarks.append(
            "Low haemoglobin level detected. Possible anemia."
        )

    if cholesterol > 200:
        remarks.append(
            "High cholesterol level detected. Increased cardiovascular risk."
        )

    if not remarks:
        remarks.append(
            "All entered health parameters are within the normal range."
        )

    return " ".join(remarks)