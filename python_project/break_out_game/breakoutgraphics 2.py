"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=(window_width-paddle_width)/2, y=window_height-PADDLE_OFFSET)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window.width - BALL_RADIUS*2)/2, (self.window.height - BALL_RADIUS*2)/2)
        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        # Initialize our mouse listeners
        # onmouseclicked()
        # onmousemoved()
        # Draw bricks
        # --First space--
        self.top_space = GRect(window_width, BRICK_OFFSET, x=0 , y=0)
        self.top_space.color = 'white'
        self.window.add(self.top_space)
        # --brick area --
        place_y = BRICK_OFFSET
        for i in range(BRICK_ROWS):
            place_x = 0
            for j in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=place_x, y=place_y)
                brick.filled = True
                if i < 2:
                    brick.color = 'red'
                    brick.fill_color = 'red'
                elif 1 < i < 4:
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                elif 3 < i < 6:
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                elif 5< i < 8:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                else:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                self.window.add(brick)
                place_x += (BRICK_WIDTH + BRICK_SPACING)

            place_y += (BRICK_HEIGHT + BRICK_SPACING)

