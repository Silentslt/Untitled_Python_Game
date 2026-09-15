import random
import time
import Game_Functions
import Player_Data
import Game_State


while True:

    if Game_State.gamestate == "Main Menu":
        Game_Functions.MainMenuLoop()

    elif Game_State.gamestate == "Playing":
        Game_Functions.GameplayLoop()

    elif Game_State.gamestate == "Loading":
        print("Loading...")

    elif Game_State .gamestate == "Creating New World":
        print("Creating world...")

    elif not Game_State.alive:
        break
