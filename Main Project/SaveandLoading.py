import Player_Data


def SaveGameHandler():
    with open("Save.txt") as file:
        for name, value in player.items:
            file.write(f"{name}={value}\n")

with open("save.txt", "r") as file:
    for line in file:
        name, value = line.strip().split("=")
        if value == "True":
            Player_Data.player[name] = True
        elif value == "False":
            Player_Data.player[name] = False
        else:
            Player_Data.player[name] = int(value)