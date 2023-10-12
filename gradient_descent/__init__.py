def line(x, coefficients):
    y = 0

    for i in range(len(coefficients)):
        y += coefficients[-i - 1] * (x**i)

    return y


def get_coordinates_x(points):
    return [i[0] for i in points]


def get_coordinates_y(points):
    return [i[1] for i in points]


def sum_of_squared_residuals(coeff, points):
    sum = 0
    for x, y in zip(get_coordinates_x(points), get_coordinates_y(points)):
        sum += (y - line(x, coeff)) ** 2

    return sum


def get_RSS_dif(_coeff, points, respect_to):
    derivative = 0
    for point in points:
        mult = -2 * (point[0] ** (len(_coeff) - respect_to - 1))
        calc = point[1] - line(point[0], _coeff)
        part_derivative = mult * calc

        derivative += part_derivative

    return derivative


def gradient_descent(coefficient_count, points, learning_rate=-1,attempts =50000):

    temp_coeff = [0 for i in range(coefficient_count)]
    temp_steps = [0 for i in range(coefficient_count)]

    if learning_rate==-1:
        match coefficient_count:
            case 0:
                # error
                pass

            case 1:
                #finding horizontal line boring
                learning_rate = 0.0003
            case 2:
                learning_rate = 0.0003 # linear
            case 3:
                learning_rate = 0.000001 # quadratic
            case 4:
                learning_rate = 0.00000003 # cubic
            case 5:
                learning = 0.0000000003 # quartic
            case default:
                pass #error

    attempts = 50000
    debug = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(attempts):
        if debug:
            print(f"iter {i}")

        for i in range(coefficient_count):
            temp_steps[i] = -learning_rate * get_RSS_dif(temp_coeff,points, i)
            if debug:
                print(f"{alphabet[i]} = {temp_coeff[i]}")
                print(f"step_{alphabet[i]} = {temp_steps[i]}")
            temp_coeff[i] += temp_steps[i]

        if debug:
            print()
        all_below = True
        for i in temp_steps:
            if abs(i) > 0.0001:
                all_below = False

        if all_below:
            break

    return temp_coeff
