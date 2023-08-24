from flask import Flask,render_template,request
import requests

api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

app = Flask(__name__)

def getTemp(weather_data,Target_date):
    for weather in weather_data:
        if weather["dt_txt"] == Target_date:
            return weather["main"]["temp"]
    return None 

def getPressure(weather_data,target_date):
    for weather in weather_data:
        if weather["dt_txt"] == target_date:
            return weather["main"]["pressure"]
    return None

def getWindSpeed(weather_data,target_date):
    for weather in weather_data:
        if weather["dt_txt"] == target_date:
            return weather["wind"]["speed"]
    return None 

@app.route("/", methods=["GET","POST"])
def index():
    result = None ; msg = "Successfully Result Generated."
    weather_data = requests.get(api_url).json()["list"]
    if request.method == "POST":
        choice = request.form["choice"]
        target_date = request.form["target_date"]
        # print(choice, target_date,len(target_date))
        result = None
        if choice == "1":
            result = getTemp(weather_data,target_date)
        elif choice == "2":
            result = getWindSpeed(weather_data,target_date)
        elif choice == "3":
            result = getPressure(weather_data,target_date)
        if len(target_date) != 19:
            msg = "Please enter valid data as input to get result Succesfully next time."

    return render_template("index.html",result = result,msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
