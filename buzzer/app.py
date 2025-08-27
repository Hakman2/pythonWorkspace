from flask import Flask
import sys
try:
    from gpiozero import Buzzer, LED
except ImportError:
    class Buzzer:
        def __init__(self, pin):
            self.pin = pin
        def on(self):
            print(f"[MOCK] Buzzer on (pin {self.pin})")
        def off(self):
            print(f"[MOCK] Buzzer off (pin {self.pin})")
    class LED:
        def __init__(self, pin):
            self.pin = pin
        def on(self):
            print(f"[MOCK] LED on (pin {self.pin})")
        def off(self):
            print(f"[MOCK] LED off (pin {self.pin})")

buzzer = Buzzer(36)#<...from the rasberry pi...> the gpio number
# Create a Flask app instance
app = Flask(__name__)

# Define a simple route
@app.route("/")
def home():
    return "Hello, Flask! 🚀 Your app is running successfully."

@app.route("/buzzer/on")
def buzzer_on():
    buzzer.on()
    return "Buzzer on."

@app.route("/buzzer/off")
def buzzer_off():
    buzzer.off()
    return "Buzzer on."

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
