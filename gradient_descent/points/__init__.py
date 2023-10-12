import random
import matplotlib.pyplot as plt
import gradient_descent as gd


def create_points(coefficients, offset_range=0.5):
    points = []
    for i in range(100):
        x = random.uniform(-10, 10)
        y = gd.line(x, coefficients)
        offset_x = random.uniform(-1.0, 1) * offset_range
        offset_y = random.uniform(-1.0, 1) * offset_range
        point = (x + offset_x, y + offset_y)
        points.append(point)
    return points




def get_scatter_points(points,plotter, color = 'b'):
    return plotter.scatter(gd.get_coordinates_x(points), gd.get_coordinates_y(points),c= color)


def draw_line(coefficients,plotter,color = 'r'):
    new_points = []
    ranges = [-10, 10]
    for i in range(ranges[0], ranges[1]):
        x = i
        y = gd.line(x, coefficients)
        point = (x, y)
        new_points.append(point)

    new_x_coordinates = [i[0] for i in new_points]
    new_y_coordinates = [i[1] for i in new_points]

    return plotter.plot(new_x_coordinates, new_y_coordinates, c=color)
