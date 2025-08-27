from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a simple route
@app.route("/")
def home():
    return "Hello, Flask! 🚀 Your app is running successfully."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
