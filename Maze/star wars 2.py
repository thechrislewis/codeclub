import random

# List of unique items to find in the rooms
items = [
    "a blaster rifle", "an Imperial keycard", "a data pad with secret plans", 
    "a thermal detonator", "a droid maintenance tool", "a lightsaber", 
    "a stormtrooper helmet", "a blaster pistol", "an old holo-recording", 
    "a TIE fighter pilot's suit", "a commlink", "a datapad with Death Star blueprints", 
    "an oxygen mask", "a thermal detonator", "a Sith holocron", "a small box of credits", 
    "a utility belt", "a deactivated droid", "a grenade launcher", "a hidden compartment with plans"
]

# Define rooms in the Death Star maze, with 20 rooms and 2 secret corridors
rooms = {
    "hangar_bay": {
        "desc": "You stand in a massive hangar bay filled with TIE fighters. The sound of heavy machinery echoes around you.",
        "north": "control_room",
        "south": "detention_block",
        "east": "corridor_1",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))  # Pop a random item
    },
    "control_room": {
        "desc": "The control room is filled with Imperial officers, staring at large screens displaying various systems on the Death Star.",
        "north": "security_tower",
        "south": "hangar_bay",
        "east": "officer_quarters",
        "west": "command_center",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "detention_block": {
        "desc": "You are in the detention block where prisoners are held. The air is cold, and the walls are lined with holding cells.",
        "north": "hangar_bay",
        "south": "trash_compactor",
        "east": "stormtrooper_barracks",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "trash_compactor": {
        "desc": "The trash compactor is a dark, damp room filled with waste and debris. The walls are closing in!",
        "north": "detention_block",
        "south": "garbage_chute",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "officer_quarters": {
        "desc": "You enter the officer quarters, where high-ranking Imperials relax. The room is decorated with lavish furniture and military insignia.",
        "north": None,
        "south": "control_room",
        "east": "communications_room",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "command_center": {
        "desc": "This is the Death Star's nerve center. A large holographic display is projecting real-time information about the galaxy's systems.",
        "north": "armory",
        "south": "control_room",
        "east": "maintenance_tunnels",
        "west": "bridge",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "armory": {
        "desc": "The armory is stocked with blasters, thermal detonators, and heavy artillery. The walls are lined with weapons caches.",
        "north": "elevator_shaft",
        "south": "command_center",
        "east": "sith_laboratory",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "maintenance_tunnels": {
        "desc": "You find yourself in the maintenance tunnels, filled with pipes and cables. The passage is narrow, and the air is stale.",
        "north": "elevator_shaft",
        "south": "garbage_chute",
        "east": None,
        "west": "command_center",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "elevator_shaft": {
        "desc": "You are in a large, vertical shaft with an elevator platform. The sounds of whirring machinery come from above and below.",
        "north": "death_star_core",
        "south": "armory",
        "east": "laser_battery",
        "west": "maintenance_tunnels",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "death_star_core": {
        "desc": "The core of the Death Star. A large, glowing superlaser sits in the center, surrounded by a high-tech control system.",
        "north": None,
        "south": "elevator_shaft",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "laser_battery": {
        "desc": "This room is filled with massive laser cannons, each capable of destroying entire planets. The walls hum with energy.",
        "north": None,
        "south": None,
        "east": "death_star_core",
        "west": "elevator_shaft",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "sith_laboratory": {
        "desc": "A dark and ominous room filled with strange equipment. It seems like experiments on the Dark Side are being conducted here.",
        "north": None,
        "south": "armory",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "stormtrooper_barracks": {
        "desc": "The barracks where stormtroopers rest. The air smells of sweat, and the room is filled with their armor and equipment.",
        "north": "detention_block",
        "south": "training_hall",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "training_hall": {
        "desc": "A large, open space where stormtroopers train in hand-to-hand combat and target practice.",
        "north": "stormtrooper_barracks",
        "south": "landing_platform",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "landing_platform": {
        "desc": "You are on a platform overlooking the Death Star's surface. Ships come and go from here.",
        "north": "training_hall",
        "south": "garbage_chute",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "garbage_chute": {
        "desc": "A narrow chute leading to the outer reaches of the Death Star. It's damp and smells faintly of refuse.",
        "north": "trash_compactor",
        "south": "landing_platform",
        "east": None,
        "west": "maintenance_tunnels",
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "communications_room": {
        "desc": "A highly secure room filled with communication equipment used for sending and receiving sensitive transmissions.",
        "north": None,
        "south": "officer_quarters",
        "east": None,
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "security_tower": {
        "desc": "A high-security tower, guarded by Imperial forces. The walls are lined with surveillance equipment.",
        "north": None,
        "south": "control_room",
        "east": "laser_battery",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },
    "bridge": {
        "desc": "The Death Star's command bridge, where the highest-ranking officers oversee the operation of the station.",
        "north": "command_center",
        "south": None,
        "east": "death_star_core",
        "west": None,
        "item": items.pop(random.randint(0, len(items)-1))
    },

    # Secret Corridors (One-way)
    "secret_corridor_1": {
        "desc": "This hidden corridor is dimly lit, with old ventilation shafts and exposed wiring. A sense of secrecy fills the air.",
        "north": "hidden_control_room",
        "south": "maintenance_tunnels",
        "east": None,
        "west": None,
        "item": "a coded Imperial message"
    },
    "secret_corridor_2": {
        "desc": "You stumble upon another secret passage, lined with damp stone and the faint echo of distant footsteps. It was clearly forgotten by most.",
        "north": "sith_tomb",
        "south": "laser_battery",
        "east": "command_center",
        "west": None,
        "item": "a rare crystal shard"
    },

    # Hidden rooms (accessible only through secret corridors)
    "hidden_control_room": {
        "desc": "A dark, secretive room filled with Imperial command consoles. It's not listed in any official maps of the Death Star.",
        "north": None,
        "south": "secret_corridor_1",
        "east": None,
        "west": None,
        "item": "a hidden cache of supplies"
    },
    "sith_tomb": {
        "desc": "An eerie room filled with ancient Sith artifacts and tombs of long-dead Sith Lords.",
        "north": None,
        "south": "secret_corridor_2",
        "east": None,
        "west": None,
        "item": "a Sith relic"
    }
}

