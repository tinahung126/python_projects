"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 80  # 120 frames per second
NUM_LIVES = 3   	# Number of attempts


def main():
    over = GLabel('Game over!')
    over.font = 'Times New Roman-30-bold'
    over.color = 'Salmon'
    win = GLabel('You Win!')
    win.font = 'Times New Roman-30-bold'
    win.color = 'tan'
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics._dx, graphics._dy)
        # Record the number of blocks.
        if graphics.is_hit_brick():
            graphics.brick_count -= 1
            # When all blocks are removed, the game is over
            if graphics.brick_count <= 0:
                graphics.window.add(win, x=(graphics.window.width - over.width)/2, y=(graphics.window.height - over.height)/2)
                break

        # When the ball hits the window, let the ball bounce.
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics._dx = -graphics._dx
        if graphics.ball.y <= 0:
            graphics._dy = -graphics._dy
        # If the ball exceeds the bottom of the window, lives - 1.
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            lives -= 1
            graphics.reset_ball_start_point()
            # If lives = 0, game over.
            if lives == 0:
                graphics.window.add(over, (graphics.window.width - over.width)/2, y=(graphics.window.height - over.height)/2)
                break


if __name__ == '__main__':
    main()
