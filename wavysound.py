from microbit import *
import music

while True:
    if button_a.is_pressed():
        music.stop()
        if button_b.is_pressed():
            break
        
    else:
        x = accelerometer.get_x()
        
        freq = x + 1024
        if freq < 10:
            freq = 10
        music.pitch(freq, -1)
