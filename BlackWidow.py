import random
from time import sleep

def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

def gas_stations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])

def gas_level_alert():
    gas_level = gas_level_gauge()
    miles_to_gas_station = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

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

    print(messages[gas_level])

print("\n****************************************\n")
print("Gasoline Branch - Developer Linus Riddle\n")

gas_level_alert()
