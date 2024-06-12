# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jake = Character("Jake", who_color="#990000")
define user = Character("You")
define truck = Character("Truck")
define god = Character("God")
define martin = Character("Martin")


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

    scene black
    ""

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
    god "Make Jake fall in love with you. The power of love is the only thing that can overcome his irreversible fate."
    user "You: What?! I can't do that!"
    god "You can. I will give you pre-made responses to every point at which Jake could die."
    god "But be careful, as my responses are not perfect. Some may accelerate his death to where even I cannot save him."
    user "You: Okay then, I think I can do it. I'll save Jake from State Farm!"
    god "Good luck my child."

    label wake_up :
        scene black
        "You hear a voice calling out to you"
        "Unknown: Hey! Are you alright?"


        scene office
        show happy-jake with dissolve
        "You open your eyes. There is a man standing in front of you."
        "You've never met him before, but you can tell from a first clance that this is the man you need to protect. This is Jake from State Farm"
        jake "Are you alright?"
        user "You: Oh yeah, sorry."
        jake "Are you new here? What's your name?"

        menu:
            "Say your Name." :
                jump name

            "Decline." :
                jump name_death

    label name_death :
        jake "Oh, okay. I guess I'll leave you be then."
        user "Okay, bye I guess"
        hide happy-jake
        "You heard later that Jake was hit by a truck after he left work"

        scene gray-bg
        show god-resized with dissolve
        god "...You had one job"
        god "How was that getting him to fall in love?"
        god "We can repeat this for as many times as it takes"
        jump wake_up


    label name :
        user "Oh, I'm (name)"
        jake "Nice to meet you (name). I'll tell you what, let's go on a tour of the office if you're new here."
        user "Sure, that sounds nice."
        jake "Alright then, let's go on a walk. Hopefully it'll wake you up a bit."
        "You head to the main office floor"
        jake "This is the office floor. This is where everybody works."
        user "Where is everybody?"
        jake "Huh. I guess they could be in the break room."
        "You head to the break room"
        jake "This is the break room. Grab some snacks or a drink if you want"
        user "Nobody here either"
        jake "Yeah, you're right. That's weird. Anyways, they could be at lunch. We should head in that direction."
        "You follow Jake as he leads you across the street to his favorite restaurant. JakeOb's Deli"
        jake "This is JakeOb's Deli. They've got some sandwiches and salads and such. What do you want to order?"

        menu:
        "Eat a Total Loss Sandwich." :
            jump total_loss

        "Eat a Salad." :
            jump salad

        "Eat a Beef Eater Sandwich" :
            jump beef

    label total_loss :
        jake "Really? Total Loss Sandwich? We work at an insurance company."
        user "I thought it would be funny"
        jake "It's not. You ruined the mood *He leaves*"
        user "Jake, wait! Don't cross the street!"
        "You see Jake get run over by a truck"

    label salad :
    jake "A salad? Alright, that's an interesting choice."
    jake "Anyways, I've gotta go real quick. Be right back. *He leaves*"
    "Unknown: Did somebody say Salad?
    "You see a very green man walk in"
    user "Uh yeah, I ordered a salad."
    martin "I loooove salad"
    user "Okay buddy"
    martin "You know, salad can help you cut off 15% or more calories"
    user "I didn't really need to know that"
    martin "*sniffs* I sense a competitor. I shall take my leave *leaves*"
    jake "*Walks back in* Alright, let's eat."
    "The two of you have an alright lunch"

    label beef :
    jake "A Beef Eater? Nice! I love those!"
    user "Yeah, I thought that you would"
    jake "I got the exact same thing."
    user "You've got good taste"
    jake "Thanks! Then, shall we eat?"
    "The two of you have a great lunch"



    # This ends the game.
    return
