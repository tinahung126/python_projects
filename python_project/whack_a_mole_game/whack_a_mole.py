"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 550
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="Whack")
# Global variables

score = 0
score_label = GLabel("Score" + str(score))
# TODO:


def main():
    score_label.font = '-20'
    window.add(score_label, 0, score_label.height)
    onmouseclicked(remove_mole)

    while True:
        mole = GImage('mole.jpeg')
        x = random.randint(0, WINDOW_WIDTH - mole.width)
        y = random.randint(0, WINDOW_HEIGHT - mole.height)
        window.add(mole, x, y)
        pause(DELAY)


def remove_mole(event):
    global score
    maybe_mole = window.get_object_at(event.x, event.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        score_label.text = 'Score:' + str(score)
if __name__ == '__main__':
    main()
