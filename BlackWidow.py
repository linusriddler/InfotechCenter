import random
from time import sleep

# Print a decorative header for the program
print("\n****************************************\n")
print("Weather Branch - Developer: Linus Riddle\n")

# Function to determine the current weather condition
def get_weather():
    return random.choice(["snowing", "blizzard", "icy", "rainy", "windy", "sunny"])

# Function to determine the vehicle response based on weather conditions
def vehicle_response_system(weather_condition):
    # Dictionary mapping weather conditions to alarm delays and speed limits
    weather_responses = {
        "snowing": (30, 55),
        "blizzard": (60, 40),
        "icy": (50, 35),
        "rainy": (20, 65),
        "windy": (15, 70)
    }

    if weather_condition in weather_responses:
        delay, speed = weather_responses[weather_condition]
        print(f"The National Weather Service has updated your alarm by {delay} minutes due to {weather_condition} conditions.")
        sleep(1)
        print(f"VRS has been engaged, only allowing us to drive {speed} MPH.")
    else:
        print(f"The National Weather Service is calling for {weather_condition} skies outside, drive safe!")
        sleep(1)
        print("VRS has been disengaged, drive safe!")

# Main execution
weather_alert = get_weather()
vehicle_response_system(weather_alert)
