# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image school = "bg girl school.jpg"
image cat = "cat.png"
#image eileen happy = "eileen happy.png"
#image eileen vhappy = "eileen vhappy.png"
define e = Character("Carrot")
define l = Character("Pineapple")

image eileen:
    "eileen happy.png"
    pause 1.0
    "eileen vhappy.png"
    pause 1.0
    repeat

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # EILEEN
    show eileen at left

    # with dissolve
    with fade
    e "Knock knock."

    # LUCY
    show lucy happy at right
    # show cat at right:
    #    xalign 1.0
    #    yalign 0.2
    l "Who's there?"

    # EILEEN
    e "Painter."

    # LUCY
    l "Painter who?"

    # EILEEN
    e "The painter, who painted all of you as mermaids..."
    e "but instead of being under water..."
    e "it's pee pee."

    # LUCY
    hide lucy
    show lucy mad at right:
        zoom 1.0
        linear 0.1 zoom 1.05
        linear 0.1 zoom 1.0
        repeat
    l "ahaha that's funny!"

    # e "Once you add a story, pictures, and music, you can release it to the world!"
    # menu:
    #    "Hey you look nice!":
    #            jump nice
    #    "Hey you look bad!":
    #            jump bad
    #label nice:
    #    show eileen vhappy at right
    #    e "I'm very happy right now!"
    #    jump scene_two
    #label bad:
    #    show eileen concerned
    #    e "Noooo"
    #    "NICE"
    #    jump scene_two

    #label scene_two:
    #e "Are we going to be okay?"

    #show eileen happy

    #e "Looking forward to it!"

    #hide eileen
    #show lucy mad

    #l "Yeah, right..."

    #hide lucy
    #show eileen vhappy

    #e "Don't be a hater"

    #show school

    # This ends the game.

    return
