input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    if (Math.randomBoolean()) {
        basic.showIcon(IconNames.Skull)
        basic.clearScreen()
        basic.showString("Heads")
    } else {
        basic.showIcon(IconNames.Square)
        basic.clearScreen()
        basic.showString("Tails")
    }
    
})
