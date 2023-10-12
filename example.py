"""
This program is a python file version of the Jupyter Notebook example.
If you don't have Jupyter Notebook already I'd recommend it

This script uses artificially generated data that roughly follows a quadratic and then with no knowledge of the original
equation tries to figure out a curve that matches the data
"""

# Import Libraries
import gradient_descent as gd
import gradient_descent.points as gd_points
import matplotlib.pyplot as plt

# Create points following a line 2x^2 -3x +4
correct_coefficients = [2,-3,4]
points_array = gd_points.create_points(correct_coefficients, point_count=200, offset_range=0.3)

# Do a train test split and print the results
train_set, test_set = gd_points.train_test_split(points_array,test_size=0.4)

print(f'Training Size = {len(train_set)}')
print(f'Testing Size = {len(test_set)}')

# Train the model to get a line with estimated parameters
trained_coefficients = gd.gradient_descent(3, points_array, debug = False)
print(f'Trained Coefficients = {trained_coefficients}')

# Draw graphs to display the data
gd_points.get_scatter_points(points_array, plt, color='y') # Plot All The point data on the graph in yellow
gd_points.draw_line(correct_coefficients, plt, color = 'r') # Plot a red line of the correct curve
gd_points.draw_line(trained_coefficients, plt, color='b') # Plot a blur line of the trained curve

# display the score of the model
print(f'Score is {gd.score(test_set,trained_coefficients)}')

plt.show()