# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jake = Character("Jake", who_color="#990000")
define user = Character("You")
define truck = Character("Truck")


# The game starts here.

label start:

    # Get user's name screen
    show screen input_screen with dissolve
    call screen input_screen
    define user = Character(_return)

    # Prologue scene
    scene gas-station-fill-page
    "You are working in a gas station. It's late at night and you're about to get off your shift."
    user "You: Finally! I'm done."
    "You walk out the door and lock up the store"
    user "You: Man, I'm tired. I can barely even think straight. Time to head home I guess."
    "You start to walk home in the dark"
    truck "*honk*"
    user "You: *Drowsily* Whaaaaa? What's that noise?"
    show truck with zoomin
    truck "*HONKKKK*"
    user "You: AHHHHH"

    # This ends the game.
    return
