"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file use the name_data to construct a line chart
with name's rank and year data. User can enter the names and
find the relation between years and ranks
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with at year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    each_year_width = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    start_point = GRAPH_MARGIN_SIZE    # The start point of x-axis
    x_position = start_point + year_index * each_year_width

    return x_position


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')     # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Lines on the left and right sides of the line chart
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # The line of each year on the line chart
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        # find name
        name = babynames.find_exact_match_name(name_data, lookup_names[i])
        if len(name) == 1:
            if name[0] in name_data:
                # storage the position
                position = {}    # Convert {year: rank} to {year: y label}
                years_rank = []  # Collect annual ranking data, if there is no data for that year, stored in '*'
                for j in range(len(YEARS)):
                    # If YEAR[j] rank data exists, convert rank to y label.
                    if str(YEARS[j]) in name_data[name[0]]:
                        y_coordinate = int(name_data[name[0]][str(YEARS[j])]) / 1000 * (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2))
                        position[str(YEARS[j])] = y_coordinate + GRAPH_MARGIN_SIZE
                        # Add the real ranking number
                        years_rank.append(name_data[name[0]][str(YEARS[j])])
                    # There is no ranking data in that year
                    else:
                        # y label will be at the bottom of the sheet
                        position[str(YEARS[j])] = str(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                        # Add the ranking data as *, which means that it doesn't have data.
                        years_rank.append('*')
                # Draw lines
                for j in range(len(YEARS)-1):
                    # Use year j and year j+1 to draw a line(The number of lines is the number of years minus one.）
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), position[str(YEARS[j])],
                                       get_x_coordinate(CANVAS_WIDTH, j+1), position[str(YEARS[j+1])], width=LINE_WIDTH, fill=COLORS[i % 4])
                # Draw ovals and texts
                for k in range(len(YEARS)):
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k) + TEXT_DX, position[str(YEARS[k])],
                                       text=f'{name[0]}, {years_rank[k]}', anchor=tkinter.SW, fill=COLORS[i % 4])
                    canvas.create_oval(get_x_coordinate(CANVAS_WIDTH, k) - 2, int(position[str(YEARS[k])]) - 2,
                                       get_x_coordinate(CANVAS_WIDTH, k) + 2, int(position[str(YEARS[k])]) + 2,
                                       fill=COLORS[i % 4], outline=COLORS[i % 4])
        else:
            print('Something wrong')

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
