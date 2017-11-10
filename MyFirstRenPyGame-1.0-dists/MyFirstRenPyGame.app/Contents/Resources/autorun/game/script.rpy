# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Carrot")
define l = Character("Pineapple")

image carrot first:
    "carrot 01.png"
    pause 1.0
    "carrot 01-blink.png"
    pause 0.15
    repeat

image carrot second:
    "carrot 02.png"
    pause 1.0
    "carrot 02-blink.png"
    pause 0.15
    repeat

image carrot third:
    "carrot 03.png"
    pause 1.0
    "carrot 03-blink.png"
    pause 0.15
    repeat

image carrot fourth:
    "carrot 04.png"
    pause 1.0
    "carrot 04-blink.png"
    pause 0.15
    repeat

image pineapple first:
    "pineapple 01.png"
    pause 1.1
    "pineapple 01-blink.png"
    pause 0.15
    repeat

image pineapple second:
    "pineapple 02.png"
    pause 1.1
    "pineapple 02-blink.png"
    pause 0.15
    repeat

image pineapple laugh:
    "pineapple 03.png"
    pause 1.1
    "pineapple 03-2.png"
    pause 0.15
    repeat

image pineapple fourth:
    "pineapple 04.png"
    pause 1.1
    "pineapple 04-blink.png"
    pause 0.15
    repeat

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # CARROT
    show carrot first:
        xalign 0.35
        yalign 0.4
    # with dissolve

    # PINEAPPLE
    show pineapple second:
        xalign 0.7
        yalign 0.4
    with fade
    # show cat at right:
    #    xalign 1.0
    #    yalign 0.2
    e "Knock knock."
    l "Who's there?"

    # CARROT
    hide carrot
    show carrot second:
        xalign 0.35
        yalign 0.4

    show brush 01-big:
        xalign 0.15
        yalign 0.2
    e "Painter."

    # PINEAPPLE
    hide pineapple
    show pineapple first:
        xalign 0.7
        yalign 0.4

    hide brush
    show brush 02-big:
        xalign 0.15
        yalign 0.2
    l "Painter who?"

    # CARROT
    hide carrot
    show carrot third:
        xalign 0.35
        yalign 0.4

    hide brush
    show tail 01:
        xalign 0.10
        yalign 0.2
    e "The painter, who painted all of you as mermaids..."

    hide tail
    show tail 02:
        xalign 0.15
        yalign 0.2
    e "but instead of being under water..."
    hide carrot
    show carrot fourth:
        xalign 0.35
        yalign 0.4

    hide tail
    show tail 03:
        xalign 0.15
        yalign 0.2
    show peepee:
        xalign 0.25
        yalign 0.2
    show brush 02:
        xalign 0.15
        yalign 0.2
    e "it's pee pee."

    # PINEAPPLE
    hide tail
    hide brush
    hide peepee
    hide pineapple
    show pineapple laugh:
        xalign 0.7
        yalign 0.4
        zoom 1.0
        linear 0.1 zoom 1.05
        linear 0.1 zoom 1.0
        repeat
    l "ahaha that's funny!"

    # PINEAPPLE & CARROT
    hide pineapple
    hide carrot
    show pineapple fourth:
        xalign 0.7
        yalign 0.4

    show carrot third:
        xalign 0.35
        yalign 0.4
    l "Oh... she's gone..."

    hide carrot
    hide pineapple
    show cat
    "Miau!!!"

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
