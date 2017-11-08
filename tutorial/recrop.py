#!/usr/bin/env python3

import re

CODE = """
image concert:
    subpixel True
    size (1280, 720)
    xalign .5
    yalign .5

    parallel:
        "concert2"
        pause 1.0

        block:
            "concert1" with Dissolve(.1)
            pause .4
            "concert2" with Dissolve(.1)
            pause .4
            "concert3" with Dissolve(.1)
            pause .4
            "concert2" with Dissolve(.1)
            pause .4
            repeat

        time 43.0

    parallel:


        # Lucy Strums.
        crop (128, 378, 252, 189)
        pause 1.0
        easeout .6 crop (160, 400, 200, 150)

        crop (65, 174, 252, 189)
        easein .8 crop (36, 138, 337, 253)

        # Mary cymbals.
        time 2.9
        crop (532, 320, 179, 134)
        time 3.4
        crop (302, 262, 236, 177)
        time 3.9
        crop (532, 320, 179, 134)
        time 4.4
        crop (302, 262, 236, 177)

        # Zoom out.
        time 5.0
        linear 4.0 crop (18, 208, 741, 556)
        easein 4.0 crop (179, 0, 1019, 764)
        easeout 4.0 crop (0, 0, 1019, 764)


        # Pan up Eileen
        time 17.0
        crop (565, 403, 483, 362)

        linear 4.0 crop (544, 0, 653, 490)

        time 22.25

        # Mary's random crops.
        block:
            choice:
                crop (397, 245, 309, 232)
            choice:
                crop (247, 275, 493, 370)
            choice:
                crop (387, 249, 321, 241)
            choice:
                crop (362, 252, 192, 144)
            choice:
                crop (272, 432, 443, 332)

            pass

            choice:
                zoom 1.0
            choice:
                zoom 1.3
            choice:
                zoom 1.5

            pause .43

            repeat

        # Lucy and Mary
        time 26.97
        zoom 1
        crop (30, 208, 741, 556)
        pause 1.0

        # Mary
        crop (30, 369, 420, 315)
        easein 5.5 crop (0, 121, 420, 315)

        # Final shot.
        easeout 4.0 crop (0, 0, 1019, 765)
        easein 4.0 crop (180, 0, 1019, 765)
"""


def update_crop(m):
    x, y, w, h = eval(m.group(1))

    x *= 2
    y *= 2
    w *= 2
    h *= 2

    y += int(h * .06)
    h = int(h * .88)

    widew = h * 16 // 9

    # print(x, y, w, h, widew)

    x -= (widew - w) // 2
    w = widew

    if x < 0:
        x = 0

    if x > 2400 - w:
        x = 2400 - w

    t = (x, y, w, h)

    return "crop {!r}".format(t)


for l in CODE.split("\n"):
    l = re.sub(r'crop (\(.*?\))', update_crop, l)
    print(l)
