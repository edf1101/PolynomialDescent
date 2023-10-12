import gradient_descent.points as gd_points
import gradient_descent as gd
import matplotlib.pyplot as plt

points_array = gd_points.create_points([2,-3,4])

gd_points.get_scatter_points(points_array,plt)
gd_points.draw_line([2,-3,4],plt)

coeff = gd.gradient_descent(3,points_array)
gd_points.draw_line(coeff,plt,color='g')
plt.show()

print(coeff)






