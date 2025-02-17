print("\n****************************************\n")
print("Gasoline Branch - Developer Linus Riddle\n")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
  return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesTOGasStationLow = round( random.uniform(1,25),1)
    milesTOGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", + milesTOGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking GPS for the closest gas station")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", + milesTOGasStationQuarterTank, "miles away.")

gasLevelAlert()