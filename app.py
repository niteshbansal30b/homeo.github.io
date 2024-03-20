from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    # Extract form data
    appointment_date = request.form['appointmentDate']
    doctor = request.form['doctor']
    name = request.form['name']
    contact = request.form['contact']
    medical_problem = request.form['medicalProblem']

    # Construct the email content
    email_body = f"Appointment Details:\n\nDate: {appointment_date}\nDoctor: {doctor}\nName: {name}\nContact: {contact}\nMedical Problem: {medical_problem}"

    # Send email (this is a simplified example; you'll need to configure it with your SMTP details)
    sender_email = "dummyguy777@yahoo.com"  # Change to your email
    receiver_emails = ["nitujaipur@gmail.com", "monikabansaljp@gmail.com"]
    password = "Mum@0619"  # Change to your email password or app-specific password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)
    message["Subject"] = "New Appointment Booking"
    message.attach(MIMEText(email_body, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:  # Change SMTP server and port
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, message.as_string())

    return jsonify({"message": "Appointment booked successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
