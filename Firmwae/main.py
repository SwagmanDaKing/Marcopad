import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Encoder-Module
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

#Pins (SW1 - SW4)
# SW1(GP1), SW2(GP2), SW3(GP4), SW4(GP3)
PINS = [board.GP1, board.GP2, board.GP4, board.GP3]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#Rotary Encoder (SW5) 
# Pin A -> GP26, Pin B -> GP27. (S1/S2) -> GP28.
encoder_handler.pins = (
    (board.GP26, board.GP29, board.GP27, board.GP28, False), 
)

#Keymap
# SW1: Next Track | SW2: Prev Track | SW3: Stop | SW4: Play/Pause
# Encoder (SW5) Mute 
keyboard.keymap = [
    [
        KC.MEDIA_NEXT_TRACK, # SW1
        KC.MEDIA_PREV_TRACK, # SW2
        KC.MEDIA_STOP,       # SW3
        KC.MEDIA_PLAY_PAUSE, # SW4
        KC.MUTE,             # Encoder Klick (SW5)
    ]
]

# 4. Encoder Turning
# [left (volume down), right (volume up)]
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),)
]

if __name__ == '__main__':
    keyboard.go()
