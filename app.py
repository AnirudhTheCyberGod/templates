from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def receive_form_data():
    try:
        # Get the form data from the request
        form_data = request.form

        # Access the form fields using the keys (e.g., form_data['name'])
        name = form_data['name']
        college = form_data['college']
        email = form_data['email']
        mobile = form_data['mobile']

        # Print the received data
        print(f"Received data: Name={name}, College={college}, Email={email}, Mobile={mobile}")

        # Create a response message that includes the received data
        response_message = f"Form data received and processed successfully!\n"
        response_message += f"Name: {name}\n"
        response_message += f"College: {college}\n"
        response_message += f"Email: {email}\n"
        response_message += f"Mobile: {mobile}\n"

        # Return the response with the message
        return response_message
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
