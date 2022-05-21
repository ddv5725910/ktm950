def on_button_pressed_a():
    for index in range(3):
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . . . .
                        . # . . .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(3):
        basic.show_leds("""
            . . # . .
                        . . . # .
                        . . . . #
                        . . . # .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
