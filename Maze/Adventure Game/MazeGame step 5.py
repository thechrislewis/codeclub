'''
Add enemies to the game
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

constructed_items = {"Magic Staff": ["Crystal Shard", "Wooden Stick", "Enchanted Core"]}
enemies = {"Dark Sorcerer": "Magic Staff"}  # Enemy that can be defeated with a specific item

def display_room():
    print(f"You appear to be in the {current_room}")
    print(rooms[current_room].get("Desc", "No description available."))
    
    if "Item" in rooms[current_room]:
        print(f"There is a {rooms[current_room]['Item']} in the room")
    else:
        print("The room is empty")
    
    if "Enemy" in rooms[current_room]:
        print(f"A {rooms[current_room]['Enemy']} is here! Be careful!")
    
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
    global current_room
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
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
            rooms[current_room]["Item"] = item
            print(f"You dropped {item}.")
        else:
            print(f"You don't have {item}.")
    elif action == "Craft":
        for crafted_item, components in constructed_items.items():
            if item == crafted_item and all(comp in inventory for comp in components):
                for comp in components:
                    inventory.remove(comp)
                inventory.append(crafted_item)
                print(f"You have successfully crafted {crafted_item}!")
                return
        print(f"You don't have the necessary components to craft {item}.")

def handle_combat():
    global current_room
    if "Enemy" in rooms[current_room]:
        enemy = rooms[current_room]["Enemy"]
        if enemy in enemies and enemies[enemy] in inventory:
            print(f"You defeated the {enemy} with your {enemies[enemy]}!")
            del rooms[current_room]["Enemy"]
        else:
            print(f"The {enemy} attacks! You need a {enemies.get(enemy, 'proper weapon')} to defeat it!")

def main():
    global current_room
    while True:
        display_room()
        if "Enemy" in rooms[current_room]:
            handle_combat()
        
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
        elif action in ["Get", "Drop", "Craft"] and argument:
            handle_item_interaction(action, argument)
        elif action == "Passcode" and argument == "8915" and current_room == "Library":
            print("Lock unlocked!")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
