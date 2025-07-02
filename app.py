from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Retrieve submitted form data
    dentist_name = request.form.get('dentistName')
    clinic_name = request.form.get('clinicName')
    whatsapp = request.form.get('whatsappNumber')
    country = request.form.get('country')
    patient_notes = request.form.get('patientNotes')
    payment_method = request.form.get('paymentMethod')

    # Retrieve uploaded files if needed
    xray_files = request.files.getlist('xrayUpload')
    oral_photos = request.files.getlist('oralPhotos')

    # For now, we do not store uploaded files – you can expand this later
    print("Form submitted successfully:")
    print(f"Doctor: {dentist_name}, Clinic: {clinic_name}, WhatsApp: {whatsapp}, Country: {country}")
    print(f"Notes: {patient_notes}, Payment: {payment_method}")
    print(f"X-rays uploaded: {len(xray_files)}, Oral Photos: {len(oral_photos)}")

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return """
    <h2>Welcome to the EpidentAI Dashboard</h2>
    <p>This is a placeholder page. More functionality will be added here soon.</p>
    <a href="/">Go back to Registration</a>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
