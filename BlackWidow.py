print("\n****************************************\n")

print("Weather Branch - Developer: Linus Riddle\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine the weather
def weather():
    weatherForcastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForcastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is currently", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
         print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is currently a", weatherAlert, "outside.")
    elif weatherAlert == "icy":
         print("\nThe National Weather Service has updated your alarm by 50 minutes because"
              " it is currently", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
         print("\nThe National Weather Service has updated your alarm by 20 minutes because"
              " it is currently", weatherAlert, "outside.")
    elif weatherAlert == "windy":
         print("\nThe National Weather Service has updated your alarm by 15 minutes because"
              " it is currently", weatherAlert, "outside.")
    else:
         print("\nThe National Weather Service is calling for", weatherAlert, "skies outside, drive safe!")

vehicleResponseSystem()