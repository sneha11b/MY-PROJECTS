# # WEATHER FORECASTER

pip install requests
import requests
print("\t\tWelcome to the Weather Forecaster")
print("Just enter the city you want the weather report")
city_name=input("Enter the name of the city:")
def Gen_report(C):
    url='https://wttr.in/{}'.format(C)
    try:
        data= requests.get(url)
        T=data.text
    except:
        T="Error Occurred"
    print(T)
Gen_report(city_name)


# # WTTR stands for "Weather in Terminal, Right Now." It is a command-line utility and a simple yet powerful tool for retrieving weather information directly from your terminal or command prompt. 
# WTTR provides weather forecasts and current conditions using data from various weather sources. 
# By accessing WTTR in your terminal, you can quickly obtain weather information for a specified location or your current location. It offers a concise and easily readable presentation of weather data, including temperature, humidity, wind speed, and conditions like rain or snow. 
# Additionally, WTTR supports various features such as displaying weather as ASCII art, providing short-term and long-term forecasts, and supporting multiple languages.
# 
# WTTR is highly customizable, allowing users to configure the output according to their preferences. 
# The utility can be accessed through a web API or directly from the command line, making it convenient for developers and users who prefer command-line interfaces.
