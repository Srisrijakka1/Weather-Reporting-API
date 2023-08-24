import requests 

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# Get the response
response = requests.get(url)

# For any request to https via request.get(): 

# 200 OK
# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 500 Internal Server Error
# so we accept only OK status not other errors
if response.ok:
    #  to access the list of weather data in the JSON response
    weather_data = response.json()["list"]
    # print(response.json()["list"])

    while True:
        print("1. Get Temperature \n2. Get Wind Speed \n3. Get Pressure\n0. Exit\n")
        choice = int(input("Enter Your choice : "))
        if choice == 0:
            print("Exit the program")
            break 
        elif choice == 1:
            input_date = input("Enter the input date and time in this formate (year-month-date hr:min:sec) : ")
            Temp_At_Input_Date = -1
            for weather in weather_data:
                if weather['dt_txt'] == input_date:
                    Temp_At_Input_Date = weather["main"]["temp"]
                    break 
            if Temp_At_Input_Date == -1:
                print("For given input date and time the Temperature is not found.")
            else:
                print("Temperature at ",input_date,"is : ",Temp_At_Input_Date) 
        elif choice == 2:
            input_date = input("Enter the input date and time in this formate (year-month-date hr:min:sec) : ") 
            WindSpeed_At_Input_Date = -1 
            for weather in weather_data:
                if weather['dt_txt'] == input_date:
                    WindSpeed_At_Input_Date = weather["wind"]["speed"] 
                    break 
            if WindSpeed_At_Input_Date == -1:
                print("For given input date and time the WindSpeed is not found.")
            else:
                print("Wind speed at ",input_date,"is : ",WindSpeed_At_Input_Date)
        elif choice == 3:
            input_date = input("Enter the input date and time in this formate (year-month-date hr:min:sec) : ") 
            Pressure_At_Input_Date = -1.0
            for weather in weather_data:
                if weather['dt_txt'] == input_date:
                    Pressure_At_Input_Date = weather["main"]["pressure"] 
                    break 
            if Pressure_At_Input_Date == -1:
                print("For given input date and time the Pressure is not found.")
            else:
                print("Pressure at ",input_date,"is : ",Pressure_At_Input_Date)
        else:
            print("You have entered an invalid choice.\nPlease Enter a valid choice: ")
else:
    print(response.json(),"Error occured while fetching weather data")