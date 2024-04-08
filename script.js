document.getElementById("healthForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission from refreshing the page

    // Get form data
    let formData = new FormData(this);

    // Convert form data to object
    let data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Validate form data
    if (!data.name || !data.age || !data.symptoms) {
        alert("Name, age, and symptoms are required fields");
        return;
    }

    // AJAX request to server for processing form data
    fetch('/submit_health_form', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("output").innerHTML = `Submission successful: ${result.message}`;
    })
    .catch(error => {
        console.error('Error submitting form:', error);
        alert("Error while submitting form. Please try again later.");
    });

    // Format and display data (optional)
    let formattedData = `Name: ${data.name}<br>Age: ${data.age}<br>Gender: ${data.gender}<br>Symptoms: ${data.symptoms}<br>Medical History: ${data.medicalHistory || 'N/A'}<br>Current Medications: ${data.medications || 'N/A'}<br>`;
    document.getElementById("output").innerHTML = formattedData;
}
