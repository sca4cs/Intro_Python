from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", True, "spear"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False, "sword club coins lantern"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, "spear katana"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, "scimitar crown"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, "katana sword chalice"),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main
print("\n\nWelcome traveler! Are you ready for an adventure?")
print("\n\nUse the following commands to move:\n    n: North\n    s: South\n    e: East\n    w: West")
print("\nYou can also type the full direction - i.e. 'north'")
print("Other valid commands include 'forward', 'backward', 'right', and 'left'")
print("\nTo pick up an item and add it to your inventory type 'get' or 'take' followed by the item name")
print("i.e. - 'take coins'")
print("\nYou can also drop an item by typing 'drop' followed by the item name")
print("To see your score, type 'score'; to see your inventory, type 'i' or 'inventory'")
print("\n\n~~~~ Good luck on your travels! ~~~~")


valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "north": "n", "south": "s", "east": "e", "west": "w",
                    "forward": "n", "backward": "s", "right": "e", "left": "w"}

valid_items = {"katana": "katana", "spear": "spear", "sword": "sword",
                    "scimitar": "scimitar", "club": "club", "lantern": "lantern",
                    "coins": "coins", "chalice": "chalice", "crown": "crown"}

nameInput = input("\n\nPlease enter your name: ")
player = Player(nameInput, room['outside'])
print(f"\n\n{player.currentRoom}")

while True:
    cmds = input("\n-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.seeInventory()
        elif cmds[0] == "score":
            player.seeScore()
        else:
            print("\n\nI did not understand that command; Press q to quit")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "get" or cmds[0] == "take":
            if cmds[1] in valid_items:
                player.pickUpItem(valid_items[cmds[1]])
        elif cmds[0] == "drop":
            if cmds[1] in valid_items:
                player.dropItem(valid_items[cmds[1]])
        else:
            print("\n\nI did not understand that command; Press q to quit")