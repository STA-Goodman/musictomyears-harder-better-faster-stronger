import winsound
import time
# eighth note = 500
# quarter note = 1000
# dotted quarter = 1500
# half note = 2000

def low_low_d(duration = 500):
    winsound.Beep(146, duration)

def low_Eb(duration = 500):
    winsound.Beep(155, duration)

def low_f(duration = 500):
    winsound.Beep(174, duration)

def low_g(duration = 500):
    winsound.Beep(196, duration)

def mid_c(duration = 500):
    winsound.Beep(261, duration)

def low_d(duration = 500):
    winsound.Beep(293, duration)

def Eb(duration = 500):
    winsound.Beep(329, duration)

def f(duration = 500):
    winsound.Beep(349, duration)

def g(duration = 500):
    winsound.Beep(392, duration)

def a(duration = 500):
    winsound.Beep(440, duration)
    
def b(duration = 500):
    winsound.Beep(493, duration)

def Bb(duration = 500):
    winsound.Beep(466, duration)

def c(duration = 500):
    winsound.Beep(523, duration)

def d(duration = 500):
    winsound.Beep(587, duration)

def high_e(duration = 500):
    winsound.Beep(659, duration)

def high_Eb(duration = 500):
    winsound.Beep(622, duration)

def high_f(duration = 500):
    winsound.Beep(698, duration)

def high_g(duration = 500):
    winsound.Beep(783, duration)

def high_a(duration = 500):
    winsound.Beep(880, duration)

def high_Bb(duration = 500):
    winsound.Beep(932, duration)

def high_c(duration = 500):
    winsound.Beep(1046, duration)

def high_d(duration = 500):
    winsound.Beep(1174, duration)

def qr(): # quarter rest
    time.sleep(2)

song = [Bb, g, d, c, Bb, g, qr, Bb, f, c, Bb, a, Bb]

def er(): # eighth rest
    time.sleep(1)
# without the parentheses after the functions, they won't be called
song = []
line1 = [Bb, g, d, c, Bb, g, qr, Bb, f, c, Bb, a, Bb, qr, high_g, high_e, high_Bb, high_a, high_g, high_e, high_Eb, high_Eb, Eb, Eb, low_Eb, low_Eb, low_low_d, low_low_d] # list of line one's notes
song.append(line1)
line2 = [er, g, Bb]
time.sleep(1)
for note in song:
    note() # parentheses here so that the list's functions are called [as a function]