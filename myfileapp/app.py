from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Configure your mail server (example using Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # your email here
app.config['MAIL_PASSWORD'] = 'your-app-password'  # your app password here
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'your-email@gmail.com')

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message_body = data.get('message')

    if not name or not email or not message_body:
        return jsonify({'error': 'Please fill in all fields.'}), 400

    msg = Message(subject="New Portfolio Contact Form Message",
                  recipients=['your-email@gmail.com'])  # your email here
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

    try:
        mail.send(msg)
        return jsonify({'message': 'Message sent successfully!'})
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Failed to send email.'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
