import winsound
import time

# eighth note = 500
# quarter note = 1000
# dotted quarter = 1500
# half note = 2000


def low_f(duration = 500):
    winsound.Beep(174, duration)

def low_g(duration = 500):
    winsound.Beep(196, duration)

def low_a(duration = 500):
    winsound.Beep(220, duration)

def low_Bb(duration = 500):
    winsound.Beep(233, duration)

def mid_c(duration = 500):
    winsound.Beep(261, duration)

def low_d(duration = 500):
    winsound.Beep(293, duration)

def e(duration = 500):
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

def eb(duration = 500):
    winsound.Beep(622, duration)

def f(duration = 500):
    winsound.Beep(698, duration)

def g(duration = 500):
    winsound.Beep(783, duration)

def qr():
    time.sleep(2)
song = [Bb, g, d, c, Bb, g, qr, Bb, f, c, Bb, a, Bb]
time.sleep(1)
for note in song:
    note()