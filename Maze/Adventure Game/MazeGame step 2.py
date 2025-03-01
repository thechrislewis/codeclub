'''
Refactored adventure game to improve code readability and maintainability.
the game functions are:
- Load game data from JSON file
- Display room description
- Handle movement between rooms
- Handle item interaction (get and drop)
- Handle passcode input
- Main game loop

'''

import json

# Load game data from JSON file
def load_game_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

game_data = load_game_data("game_data.json")
rooms = game_data["rooms"]
current_room = game_data["start"]
inventory = []

def display_room():
    print(f"You appear to be in the {current_room}")
    print(rooms[current_room].get("Desc", "No description available."))
    
    if "Item" in rooms[current_room]:
        print(f"There is a {rooms[current_room]['Item']} in the room")
    else:
        print("The room is empty")
    
    if inventory:
        print(f"You have {len(inventory)} items: {', '.join(inventory)}")
    else:
        print("You have no items!")

def handle_movement(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f"You moved {direction}")
    else:
        print("You can't go that way.")

def handle_item_interaction(action, item):
    if action == "Get":
        if "Item" in rooms[current_room] and rooms[current_room]["Item"].lower() == item.lower():
            if item not in inventory:
                inventory.append(item)
                del rooms[current_room]["Item"]
                print(f"{item} retrieved!")
            else:
                print(f"You already have the {item}.")
        else:
            print(f"Can't find {item}.")
    ## Add drop action

    ## Are there any other actions??

def main():
    global current_room
    while True:
        display_room()
        user_input = input("Enter command\n").strip().split(" ")
        
        if not user_input:
            continue
        
        action = user_input[0].title()
        argument = " ".join(user_input[1:]).title() if len(user_input) > 1 else ""

        if action == "Exit":
            print("Goodbye!")
            break
        elif action == "Go" and argument in ["North", "South", "East", "West", "Up", "Down", "Out", "In"]:
            handle_movement(argument)
        elif action in ["Get", "Drop"] and argument:
            handle_item_interaction(action, argument)
        elif action == "Passcode" and argument == "8915" and current_room == "Library":
            print("Lock unlocked!")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
