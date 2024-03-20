#!/usr/bin/env python3
import cgi
import sys

try:
    # Print HTTP header
    print("Content-Type: text/html")
    print()

    # Retrieve form data
    form = cgi.FieldStorage()

    # Extract form fields
    name = form.getvalue('name', '')
    age = form.getvalue('age', '')
    gender = form.getvalue('gender', '')
    symptoms = form.getvalue('symptoms', '')
    medical_history = form.getvalue('medical_history', '')
    medications = form.getvalue('medications', '')
    allergies = form.getvalue('allergies', '')
    lifestyle = form.getvalue('lifestyle', '')

    # Check for required fields
    if not name or not age:
        raise ValueError("Name and age are required fields")

    # Format the data
    data = f"Name: {name}<br>"
    data += f"Age: {age}<br>"
    data += f"Gender: {gender}<br>"
    data += f"Symptoms: {symptoms}<br>"
    data += f"Medical History: {medical_history}<br>"
    data += f"Medications: {medications}<br>"
    data += f"Allergies: {allergies}<br>"
    data += f"Lifestyle: {lifestyle}<br>"
    data += "--------------------------------------<br>"

    # Save the data to a file (optional)
    with open('form_responses.txt', 'a') as file:
        file.write(data)

    # Display response HTML
    print("<html><head><title>Form Submission Response</title></head><body>")
    print("<h1>Form Submission Successful!</h1>")
    print("<p>Thank you for submitting the form.</p>")
    print("<p>Your data:</p>")
    print(data)
    print("</body></html>")

except Exception as e:
    # Error handling
    print("<html><head><title>Error</title></head><body>")
    print("<h1>Error</h1>")
    print(f"<p>An error occurred: {str(e)}</p>")
    print("</body></html>")
    # Log the error to stderr
    print(f"Error: {str(e)}", file=sys.stderr)

