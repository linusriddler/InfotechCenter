# Importing required libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Provides time-related functions, including sleep

# Print a welcome message with the developer's name
print("\nWelcome Branch - Developer: Linus Riddle\n")

# Print the version of the system
print("\tWelcome to InfoTechCenter V1.0\n")

# Initialize variables for controlling the loop and dot animation
x = 0  # Counter for the number of iterations
ellipsis = 0  # Controls the number of dots in the loading message

# Begin a while loop to simulate the boot process
while x != 20:  # Loop will run 20 times
    x += 1  # Increment the loop counter
    message = ("InfoTech Center System Booting" + "." * ellipsis)  # Create the message with dots
    ellipsis += 1  # Increase the number of dots after the message
    sys.stdout.write("\r" + message)  # Print the message, overwriting the previous line
    time.sleep(.5)  # Wait for 0.5 seconds to simulate loading time
    if ellipsis == 4:  # Reset dots after 3 dots (as 4 dots would be a reset)
        ellipsis = 0
    if x == 20:  # When the loop reaches 20 iterations, print boot completion message
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
