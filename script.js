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

    // Format data (optional)
    let formattedData = `Name: ${data.name}<br>Age: ${data.age}<br>Gender: ${data.gender}<br>Symptoms: ${data.symptoms}<br>Medical History: ${data.medicalHistory || 'N/A'}<br>Current Medications: ${data.medications || 'N/A'}<br>`;

    // Display formatted data (optional)
    document.getElementById("output").innerHTML = formattedData;

    // Save the data to a file (optional)
    // Example: You can use AJAX to send the data to a server-side script for processing and saving to a file/database
});
