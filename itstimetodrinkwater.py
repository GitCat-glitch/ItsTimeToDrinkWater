import pygame
from win10toast import ToastNotifier
import configparser as cp
import time

# Read configuration file
config = cp.ConfigParser()
config.read("config.ini")

filename = config.get("configure", "sound")
waittime = config.get("configure", "seconds")

# Initialize notification
toaster = ToastNotifier()

# Show the initial notification
toaster.show_toast(
    "ItsTimeToDrinkWater is running in the background!",
    "You can close it by task manager.",
    duration=10
)

# Main loop to play sound and show notifications
while True:
    time.sleep(int(waittime))
    pygame.mixer.init()

    # Load and play the sound
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Show the "drink water" notification
    toaster.show_toast(
        "It's time to Drink Water!",
        "Go and drink some water!\nRecommended: 500ml",
        duration=10
    )
