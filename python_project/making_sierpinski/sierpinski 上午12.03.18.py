"""
File: sierpinski.py
Name: Tina Hung
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 3	               # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This function is to determine the levels of triangle and draw the Sierpinski Triangle.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	This function draws Sierpinski triangle based on ORDER amount.
	:param order: Controls the order of Sierpinski Triangle
	:param length: The length of order 1 Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle
	"""
	if order == 0:
		# Base case
		pass
	else:
		# The upper line of triangle
		upper_line = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		# The left-side line of triangle
		left_side = GLine(upper_left_x, upper_left_y, upper_left_x + length*0.5, upper_left_y + length * 0.866)
		# The right-side line of triangle
		right_side = GLine(upper_left_x + length, upper_left_y, upper_left_x + length - length * 0.5, upper_left_y+length*0.866)
		window.add(upper_line)
		window.add(left_side)
		window.add(right_side)
		# Create three smaller triangles.
		# The upper left smaller triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# The upper right smaller triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length / 2, upper_left_y)
		# The bottom smaller triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length/2 * 0.866)

if __name__ == '__main__':
	main()