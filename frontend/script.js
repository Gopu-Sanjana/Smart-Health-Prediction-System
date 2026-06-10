const API_URL = "http://127.0.0.1:8000";

let editingPatientId = null;

document
    .getElementById("patientForm")
    .addEventListener("submit", createPatient);

async function createPatient(event) {

    event.preventDefault();

    const patientData = {

        full_name:
        document.getElementById("full_name").value,

        date_of_birth:
        document.getElementById("dob").value,

        email:
        document.getElementById("email").value,

        glucose:
        Number(document.getElementById("glucose").value),

        haemoglobin:
        Number(document.getElementById("haemoglobin").value),

        cholesterol:
        Number(document.getElementById("cholesterol").value)
    };

    // Validation

    if (new Date(patientData.date_of_birth) > new Date()) {

        alert("Date of Birth cannot be in the future");
        return;
    }

    if (patientData.glucose <= 0) {

        alert("Glucose must be greater than 0");
        return;
    }

    if (patientData.haemoglobin <= 0) {

        alert("Haemoglobin must be greater than 0");
        return;
    }

    if (patientData.cholesterol <= 0) {

        alert("Cholesterol must be greater than 0");
        return;
    }

    try {

        let url =
        `${API_URL}/patients`;

        let method =
        "POST";

        if (editingPatientId) {

            url =
            `${API_URL}/patients/${editingPatientId}`;

            method =
            "PUT";
        }

        const response =
        await fetch(
            url,
            {
                method: method,

                headers: {
                    "Content-Type": "application/json"
                },

                body:
                JSON.stringify(patientData)
            }
        );

        const result =
        await response.json();

        document.getElementById("result").innerHTML = `
            <div class="alert alert-success">
                <h4>Prediction Result</h4>
                <hr>
                <p>${result.remarks || "Patient saved successfully"}</p>
            </div>
        `;

        document.getElementById("patientForm").reset();

        editingPatientId = null;

        loadPatients();

    }
    catch (error) {

        document.getElementById("result").innerHTML = `
            <div class="alert alert-danger">
                Failed to connect to API or Email already exists
            </div>
        `;

        console.error(error);
    }
}

async function loadPatients() {

    try {

        const response =
        await fetch(`${API_URL}/patients`);

        const patients =
        await response.json();

        let rows = "";

        patients.forEach(patient => {

            rows += `
            <tr>

                <td>${patient.id}</td>

                <td>${patient.full_name}</td>

                <td>${patient.email}</td>

                <td>${patient.remarks}</td>

                <td>

                    <button
                        class="btn btn-warning btn-sm me-2"
                        onclick="editPatient(${patient.id})">
                        Edit
                    </button>

                    <button
                        class="btn btn-danger btn-sm"
                        onclick="deletePatient(${patient.id})">
                        Delete
                    </button>

                </td>

            </tr>
            `;
        });

        document.getElementById("patientTable").innerHTML = rows;

    }
    catch (error) {

        console.error(error);
    }
}

async function deletePatient(id) {

    const confirmDelete =
    confirm("Delete this patient?");

    if (!confirmDelete) {
        return;
    }

    await fetch(
        `${API_URL}/patients/${id}`,
        {
            method: "DELETE"
        }
    );

    loadPatients();
}

async function editPatient(id) {

    const response =
    await fetch(
        `${API_URL}/patients/${id}`
    );

    const patient =
    await response.json();

    document.getElementById("full_name").value =
    patient.full_name;

    document.getElementById("email").value =
    patient.email;

    document.getElementById("dob").value =
    patient.date_of_birth;

    document.getElementById("glucose").value =
    patient.glucose;

    document.getElementById("haemoglobin").value =
    patient.haemoglobin;

    document.getElementById("cholesterol").value =
    patient.cholesterol;

    editingPatientId = id;
}

loadPatients();