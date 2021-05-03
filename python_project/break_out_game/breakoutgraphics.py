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
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_count = brick_cols * brick_rows  # The total bricks amount.
        self.ball_radius = ball_radius

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
        self._dx = 0
        self._dy = 0
        self.__switch = True      # To control the mouse click event

        # Initialize our mouse listeners
        onmousemoved(self.move_brick)
        onmouseclicked(self.start_game)
        # Draw bricks
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset
        self.draw_bricks()

    def start_game(self, event):
        """
        When the user clicks the mouse and the switch value is True, then start processing this method.
        If the switch value is False, it can't enter the while loop.
        :param event: mouse click event
        """
        while self.__switch:
            # To avoid mouse click event
            self.__switch = False
            self.set_ball_velocity()

    def set_ball_velocity(self):
        """
        Set the ball velocity.
        Random the x velocity, and fixed the y velocity.
        :return:
        """
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx
        if random.random() > 0.5:
            self._dy = -self._dy

    def reset_ball_start_point(self):
        """
        Restart the mouse click event, and reset the ball position to the initial position.
        """
        self.__switch = True
        self.ball.x = (self.window.width - BALL_RADIUS * 2) / 2
        self.ball.y = (self.window.height - BALL_RADIUS * 2) / 2
        # Let the ball stop moving
        self._dx = 0
        self._dy = 0

    def is_hit_brick(self):
        """
        Check whether the four corners of the ball touch other objects.
        If the ball hits the paddle, turn  dy to -dy and let the ball bounce. -Return False
        If the ball hits any brick, remove the brick and turn dy to -dy. -Return True
        :return True or False:
        """
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                if self.window.get_object_at(self.ball.x + self.ball_radius * i, self.ball.y + self.ball_radius * j) is not None:
                    # If the ball hits an object, and the ball position is in the bricks area
                    if self.ball.y < (BRICK_OFFSET + (self.brick_rows - 1) * self.brick_spacing + self.brick_rows * self.brick_height):
                        find_obj = self.window.get_object_at(self.ball.x + self.ball_radius * i, self.ball.y + self.ball_radius * j)
                        self._dy = -self._dy
                        self.window.remove(find_obj)
                        return True
                    else:
                        # If ball is under the bricks area, change dy to -dy
                        if self._dy > 0:  # Prevent the ball from bouncing repeatedly
                            if self.ball.y + 2 * self.ball_radius > self.paddle.y:
                                self.ball.y = self.paddle.y - 2 * self.ball_radius

                                self._dy = -self._dy
                        return False

    def move_brick(self, event):
        """
        Display the paddle as a fixed y position, allowing the user to control the x position according to
        the mouse event.
        :param event: mouse move event
        """
        self.paddle.x = event.x - self.paddle.width/2
        if event.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        self.window.add(self.paddle)

    def draw_bricks(self):
        """
        Create the brick and set their colors.
        """
        place_y = self.brick_offset
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
                elif 5 < i < 8:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                else:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                self.window.add(brick)
                place_x += (BRICK_WIDTH + self.brick_spacing)
            place_y += (BRICK_HEIGHT + self.brick_spacing)
