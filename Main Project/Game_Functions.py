import random
import time

import Player_Data
import Game_State


def GainStone():
    Player_Data.player["Stone"] += random.randint(1, 8)


def GainWood():
    Player_Data.player["Wood"] += random.randint(1, 10)


def GainFood():
    Player_Data.player["Food"] += random.randint(1, 12)


def EatFood():
    Player_Data.player["Hunger"] -= Player_Data.player["Food"]

    if Player_Data.player["Hunger"] < 0:
        Player_Data.player["Hunger"] = 0

    Player_Data.player["Food"] = 0


def DrinkWater():
    Player_Data.player["Thirst"] -= Player_Data.player["Water"]

    if Player_Data.player["Thirst"] < 0:
        Player_Data.player["Thirst"] = 0

    Player_Data.player["Water"] = 0


def BecomeThirsty():
    Player_Data.player["Thirst"] += random.randint(1, 5)


def BecomeHungry():
    Player_Data.player["Hunger"] += random.randint(1, 5)


def Exploring():
    print("You explore the area...")

    GainWood()
    GainFood()

    print("Amount Of Wood:", Player_Data.player["Wood"])
    print("Amount Of Food:", Player_Data.player["Food"])

    time.sleep(0.5)

    BecomeThirsty()
    print("You Have Become More Thirsty")

    time.sleep(0.5)

    BecomeHungry()
    print("You Have Become More Hungry")

    time.sleep(1.5)


def MainMenu():
    print("\nWelcome To The Game")
    time.sleep(1)

    print("1. LOAD GAME")
    time.sleep(0.2)

    print("2. NEW GAME")
    time.sleep(0.2)

    print("3. SETTINGS")
    time.sleep(0.2)

    print("4. QUIT GAME")


def ChoiceHandler():
    return input("\nEnter Your Choice: ")


def GameMenu():
    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Inventory")
    print("3. Stats")
    print("4. Drink Water")
    print("5. Eat Food")
    print("6. Save Game")
    print("7. Return To Main Menu")


def SettingsMenu():
    print("\nSettings")
    print("1. Audio")
    print("2. Graphics")
    print("3. Back")


def MainMenuLoop():

    while Game_State.gamestate == "Main Menu":

        MainMenu()
        choice = ChoiceHandler()

        if choice == "1":
            print("\nLoading game...")

            Game_State.gamestate = "Loading"
            time.sleep(3)

            Game_State.alive = True
            Game_State.gamestate = "Playing"

        elif choice == "2":
            print("\nCreating new world...")

            Game_State.gamestate = "Creating New World"
            time.sleep(3)

            Game_State.alive = True
            Game_State.gamestate = "Playing"

        elif choice == "3":
            Game_State.gamestate = "Settings Menu"

        elif choice == "4":
            print("\nGoodbye!")

            Game_State.alive = False
            Game_State.gamestate = "Quit"

            break

        else:
            print("\nInvalid choice!")


def GameplayLoop():

    while Game_State.alive and Game_State.gamestate == "Playing":

        GameMenu()
        choice = ChoiceHandler()

        if choice == "1":
            Exploring()

        elif choice == "2":
            print("\nInventory:")
            print("Wood:", Player_Data.player["Wood"])
            print("Stone:", Player_Data.player["Stone"])
            print("Iron:", Player_Data.player["Iron"])
            print("Diamonds:", Player_Data.player["Diamonds"])
            print("Food:", Player_Data.player["Food"])
            print("Water:", Player_Data.player["Water"])

        elif choice == "3":
            print("\nStats:")
            print("Health:", Player_Data.player["Health"])
            print("Hunger:", Player_Data.player["Hunger"])
            print("Thirst:", Player_Data.player["Thirst"])
            print("Monsters Killed:", Player_Data.player["Monsters_Killed"])
            print("Days Survived:", Player_Data.player["Days_Survived"])

        elif choice == "4":
            DrinkWater()

            print("Drinking Water")
            time.sleep(2)

        elif choice == "5":
            EatFood()

            print("Eating Food")
            time.sleep(2)

        elif choice == "6":
            print("\nGame saved!")

        elif choice == "7":
            print("\nReturning to main menu...")

            Game_State.gamestate = "Main Menu"

        else:
            print("\nInvalid choice!")