"""
Gradient Descent module written by https://github.com/edf1101/ for my University Computer Science Degree

This submodule is used for creating sets of random points and for displaying them using matplotlib,
ie mainly for demo purposes.

## External Modules needed
- Random library for generating random points / offsets
- If you want to use any of the graph plotting features you need matplotlib imported
  in the code where you call the functions
"""

import random
import gradient_descent as gd


def create_points(coefficients, point_count=100, offset_range=0.5):
    """
    Creates a set of random points that follow a line with (optionally) a slight offset

    :param coefficients: The coefficients of the line to follow
    :param point_count: how many points to generate (default = 100)
    :param offset_range: How big you want the offset to be from actual line
    :return: Array of points
    """

    points = []
    for i in range(point_count):
        x = random.uniform(-10, 10)  # random x position between -10 - 10
        y = gd.line(x, coefficients)  # calculate correct y position from that

        # add offsets then append point to the list
        offset_x = random.uniform(-1.0, 1) * offset_range
        offset_y = random.uniform(-1.0, 1) * offset_range
        point = (x + offset_x, y + offset_y)
        points.append(point)
    return points


def train_test_split(points, test_size=0.3):
    """
    Split the points dataset up into a train test split set
    :param points: The points to split up
    :param test_size: How big the test size should be
    :return: 2 arrays ( train set, test set)
    """
    random.shuffle(points)
    split = int(len(points) * test_size)  # if array is 100 long this will be 30
    train = points[split:]
    test = points
    return train, test


def get_scatter_points(points, plotter, color="b"):
    """
    Plots a scatter graph of points

    :param points: points to plot
    :param plotter: reference to the matplotlib class in the script this gets called from (usually 'plt)
    :param color: Colour of the scatter points
    :return: The plotted graph (not very useful)
    """
    return plotter.scatter(
        gd.get_coordinates_x(points), gd.get_coordinates_y(points), c=color
    )


def draw_line(coefficients, plotter, color="r"):
    """
    Plots a line graph

    :param coefficients: The coefficients of curve to plot
    :param plotter: reference to the matplotlib class in the script this gets called from (usually 'plt)
    :param color: Colour of the line
    :return: The plotted graph (not very useful)
    """

    new_points = []
    ranges = [-10, 10]

    # create uniformly distributed points in range of -10,10
    for i in range(ranges[0], ranges[1]):
        x = i
        y = gd.line(x, coefficients)
        point = (x, y)
        new_points.append(point)

    new_x_coordinates = [i[0] for i in new_points]
    new_y_coordinates = [i[1] for i in new_points]

    return plotter.plot(new_x_coordinates, new_y_coordinates, c=color)
