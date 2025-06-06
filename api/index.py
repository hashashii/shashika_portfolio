from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-cv')
def download_cv():
    # Path relative to static folder
    return send_from_directory('static/cv', 'Shashika_Lakshan_CV.pdf', as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill out all fields.', 'error')
        return redirect(url_for('index') + '#contact')

    # For demo: print form data to console, here you can integrate email sending or DB storage
    print(f"Contact form submission:\nName: {name}\nEmail: {email}\nMessage: {message}")

    flash('Thank you for your message! I will get back to you soon.', 'success')
    return redirect(url_for('index') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)