# Import required libraries
import sys  # Provides access to system-specific functions
import time  # Provides time-related functions like sleep
import random
from time import sleep

# ANSI escape codes for adding colors to terminal output
RED = "\033[91m"     # Red color for critical messages
GREEN = "\033[92m"   # Green color for system success messages
YELLOW = "\033[93m"  # Yellow color for loading animation
CYAN = "\033[96m"    # Cyan color for welcome messages
RESET = "\033[0m"    # Reset color to default after each message

# Print a welcome message with the developer's name
print(CYAN + "\nWelcome Branch - Developer: Linus Riddle\n" + RESET)

# Print the version of the system
print(GREEN + "\tWelcome to InfoTechCenter V1.0\n" + RESET)

# Initialize variables for controlling the loop and dot animation
x = 0  # Counter for the number of iterations in the loop
ellipsis = 0  # Controls the number of dots displayed in the loading message

# Begin a while loop to simulate the boot process with an animated effect
while x != 20:  # Loop will run 20 times to simulate booting progress
    x += 1  # Increment the loop counter
    
    # Create the loading message with a dynamic number of dots
    message = YELLOW + "InfoTech Center System Booting" + "." * ellipsis + RESET  
    
    ellipsis += 1  # Increase the number of dots for animation effect
    
    # Print the message, overwriting the previous line for smooth animation
    sys.stdout.write("\r" + message)
    sys.stdout.flush()  # Flush the output buffer to ensure real-time updates
    
    time.sleep(0.5)  # Pause for 0.5 seconds to simulate loading time
    
    if ellipsis == 4:  # Reset the dots after reaching 3 (creates looping effect)
        ellipsis = 0

# When the loop reaches 20 iterations, display the boot completion message
print(RED + "\n\nOperating System Booted Up - Retina Scanned - Access Granted" + RESET)


import random
from time import sleep

# Display program header
print("\n****************************************\n")
print("Gasoline Branch - Developer Linus Riddle\n")

# Function to randomly select a gas level
def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to randomly select a gas station
def gas_stations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])


# Function to check gas level and determine next actions
def gas_level_alert():
    # Get current gas level
    gas_level = gas_level_gauge()

    # Define random distances for gas stations based on gas levels
    miles_to_gas_station = {
        "Low": round(random.uniform(1, 25), 1),  # Closer station for low fuel
        "Quarter Tank": round(random.uniform(25.1, 50), 1)  # Further station for quarter tank
    }

    # Predefined messages for different gas levels
    messages = {
        "Empty": "****WARNING - YOU ARE OUT OF GAS****\nCalling AAA...",
        "Low": f"Your gas tank is extremely low, checking GPS for the closest gas station...\n"
               f"The closest gas station is {gas_stations()} which is {miles_to_gas_station['Low']} miles away.",
        "Quarter Tank": f"Your gas tank is at a Quarter Tank, checking GPS for the closest gas station...\n"
                        f"The closest gas station is {gas_stations()} which is {miles_to_gas_station['Quarter Tank']} miles away.",
        "Half Tank": "Your gas tank is Half Full, plenty to get to your destination!",
        "Three Quarter Tank": "Your gas tank is Three Quarters Full!",
        "Full Tank": "Your gas tank is FULL, Vroom Vroom!"
    }

    # Print the corresponding message based on the gas level
    print(messages[gas_level])


# Execute the gas level alert function
gas_level_alert()
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
