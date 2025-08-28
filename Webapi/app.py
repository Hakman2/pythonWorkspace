from flask import Flask, render_template, request
from aibot import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            result = get_weather(city)
            if "error" in result:
                error = result["error"]
            else:
                response = (
                    f"The weather in {result['city']}, {result['country']} is "
                    f"{result['weather']} with {result['temp']}°C. "
                    f"(Lon: {result['lon']}, Lat: {result['lat']})"
                )
        else:
            error = "Please enter a city name."

    return render_template("index.html", response=response, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
