# Import required libraries
import sys  # Provides access to system-specific functions
import time  # Provides time-related functions like sleep

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
