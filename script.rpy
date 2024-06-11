# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jake = Character("Jake", who_color="#990000")
define user = Character("You")
define truck = Character("Truck")
define god = Character("God")


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

    # Chapter 0.5
    scene gray-bg
    show god-resized with dissolve
    god "Hello my child"
    user "You: God? Is that you?"
    god "Yes my child"
    user "You: Was that a truck"
    god "Yes my child"
    user "You: Why am I here?"
    god "Yes my child"
    user "You: What?"
    god "I mean...You have a glorious purpose. You see, there is a man I care for very much. His name is Jake from State Farm."
    user "You: Jake who?"
    god "From State Farm"
    user "You: No, what's his last name?"
    god "From State Farm"
    user "You: Wow that is a stupid last name"
    god "It's Greek."
    user "You: Okayyy then. What about Mr. From State Farm?"
    god "You see, his fate is incredibly strong. Without my intervention, he will inevitably be hit by a truck."
    user "You: So why don't you do something about it?"
    god "This is me doing something about it. Making you do something about it."
    user "You: Lame. What do I need to do?"

    # This ends the game.
    return
