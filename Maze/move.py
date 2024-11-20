#move tutorial

'''A tutorial to demonstrate moving between rooms'''


rooms = {
    'Hall': {
        'Desc': 'The start of the journey',
        'North': 'Library'
        },
    'Library': {
        'Desc':'The Library is full of old musty books',
        'South': 'Hall'
        }
    }

current_room = "Hall"
home = "Hall"

'''
if your version of python does not support f-strings
then you can use the format() function

name = "Ram"
age = 22
message = "My name is {0} and I am {1} years \
                    old. {1} is my favorite \
                    number.".format(name, age)
'''

# Game loop

while True:
    print(f"You appear to be in the {current_room}") # fstrings replace format command below
    print("Maybe you are not in the {0} but in the {1}".format(current_room, "cupboard under the stairs"))
    

    user_input = input("Enter command\n")
    commands = user_input.split(' ') #split user_input into list of words using the 'space' as the separator

    #process the commands
    action = commands[0].title()
    direction = ""
    msg = ""

    if len(commands) > 1:
        direction = commands[1:]
        direction = " ".join(direction).title()

    # process the action
    if action == "Exit":  
        break

    elif action == 'Go' and direction in ['North', 'South', 'East', 'West']:

           # try something and if it fails then execute the except code
        try:
            current_room = rooms[current_room][direction]
            msg = f"You moved {direction}"

        except:
            msg = "You can't go that way."

    
    elif action == "Home":
        current_room = home
        msg = "You are Home"

    else:
        msg = f"Invalid command: {user_input}"

    print(msg)
    print()
    print("***************************")


## outside of the game loop
print("Goodbye!!")
      
        
'''
UPGRADES:

1. Add diffrent directions ( Up, Down, South East etc. )
2. Create a bigger map with your own choice of theme 

'''


    

    
 
