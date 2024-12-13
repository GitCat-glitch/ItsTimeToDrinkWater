import pygame
from plyer import notification
import configparser as cp
import time

config = cp.ConfigParser()
config.read("config.ini")

filename = config.get("configure", "sound") 
waittime = config.get("configure", "seconds") 

notification.notify(
    title='ItsTimeToDrinkWater is running on background!',
    app_name = "ItsTimeToDrinkWater v0.1.0",
    message='you can close it by task manager.',
    timeout=10
)

while True:
    time.sleep(int(waittime))
    pygame.mixer.init()

    pygame.mixer.music.load(filename=filename)
    pygame.mixer.music.play()
    notification.notify(
        title='It\'s  to Drink Water!',
        app_name = "ItsTimeToDrinkWater v0.1.0",
        message='Go and drink some water!\nRecommended: 500ml',
        timeout=10
    )