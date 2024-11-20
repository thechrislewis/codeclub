#inventory tutorial

'''A tutorial to demonstrate collecting items from a room'''

inventory = [] # a list to store any items collected


# rooms is a dictionary 
rooms = {
    'room': {
        'Item': 'Light',
        'Desc': 'A room with no windows'
        }
    }

current_room = "room"
msg = ""


while True:
    print(f"You are in the {current_room}")
    
    if "Desc" in rooms[current_room].keys():
         print(rooms[current_room]['Desc'])
    
    if "Item" in rooms[current_room].keys():
        print(f"There is a {rooms[current_room]['Item']} in the room")
    else:
        print("The room is empty")

    if len(inventory) > 0:
        print(f"You have {len(inventory)} items")
        print(inventory)

    user_input = input("Enter command\n")
    commands = user_input.split(' ') # split user input into list of words separated by spaces

    # process the commands
    action = commands[0].title() # first word will be a command Title() means title case so word has capitalised first letter
    item = "Item"

    ## this is the status message after a command is carried out
    msg = "" 

    # if user_input has more than 1 word
    if len(commands) > 1:
        item = commands[1:]  # remove the action part of the command
        item = " ".join(item).title()


    if action == "Exit":
        break
        
    elif action == 'Get':
        print("Getting from Room: ", rooms[current_room])

        try:
            # Check if the item you want is the same as item in the room
            if item == rooms[current_room]["Item"]:

                if item not in inventory:
                    inventory.append(rooms[current_room]["Item"]) # add item to inventory
                    rooms[current_room].pop("Item") # remove item from the room list
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"

    elif action == "Drop":
        try:

            if item in inventory:
                inventory.remove(item)  # remove item from inventory
                rooms[current_room]["Item"] = item  # add item to the room
                print(rooms[current_room])
        except:
            msg = f"Couldn't drop {item}"
            


    else:  #if all else fails
        msg = f"Invalid command: {action}"

    print(msg)
    print()
    print("***************************")
        
## outside of game loop
print("Goodbye!!")

    
'''
UPGRADES:

1. Add and extra room
2. Add code to move between them ( hint: see move.py )

'''
