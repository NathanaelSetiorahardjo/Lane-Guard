from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    # This looks inside the 'templates' folder and serves our HTML file
    return render_template('index.html')

if __name__ == '__main__':
    # Run the server on all available IP addresses (0.0.0.0) on port 5000
    # This is what allows other phones/laptops on your Wi-Fi to connect!
    print("Starting Lane-Guard Web Server...")
    app.run(host='0.0.0.0', port=5000, debug=True)