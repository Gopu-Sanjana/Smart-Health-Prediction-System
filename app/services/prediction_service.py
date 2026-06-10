def generate_health_remark(
        glucose,
        haemoglobin,
        cholesterol):

    remarks = []

    if glucose > 200:
        remarks.append(
            "High glucose detected. Possible diabetes risk."
        )
    elif glucose > 140:
        remarks.append(
            "Borderline glucose level."
        )
    else:
        remarks.append(
            "Normal glucose level."
        )

    if haemoglobin < 12:
        remarks.append(
            "Low haemoglobin detected. Possible anemia."
        )
    else:
        remarks.append(
            "Healthy haemoglobin level."
        )

    if cholesterol > 240:
        remarks.append(
            "High cholesterol risk."
        )
    elif cholesterol > 200:
        remarks.append(
            "Moderately elevated cholesterol."
        )
    else:
        remarks.append(
            "Normal cholesterol level."
        )

    return " ".join(remarks)