def on_button_pressed_a():
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    if Math.random_boolean():
        basic.show_icon(IconNames.SKULL)
        basic.clear_screen()
        basic.show_string("Heads")
    else: 
        basic.show_icon(IconNames.SQUARE)
        basic.clear_screen()
        basic.show_string("Tails")
input.on_button_pressed(Button.A, on_button_pressed_a)