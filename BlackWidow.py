# Print a decorative header for the program
print("\n****************************************\n")

# Display program title and developer name
print("Weather Branch - Developer: Linus Riddle\n")

# Import necessary libraries
import random  # Used to randomly select a weather condition
from time import sleep  # (Unused in the current code but can be used for delays if needed)

# Function to determine the current weather condition
def weather():
    # List of possible weather conditions
    weatherForcastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    
    # Randomly choose a weather condition from the list
    weatherCondition = random.choice(weatherForcastList)
    
    # Return the selected weather condition
    return weatherCondition

# Call the weather function to get the current weather condition
weatherAlert = weather()

# Function to determine the vehicle response based on weather conditions
def vehicleResponseSystem():
    # Check different weather conditions and adjust the alarm time accordingly
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
        # Default case for sunny weather
        print("\nThe National Weather Service is calling for", weatherAlert, "skies outside, drive safe!")

# Call the function to display the appropriate weather-based response
vehicleResponseSystem()
