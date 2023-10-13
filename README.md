# Gradient Descent Module
 _Gradient Descent for the Fundamentals of Machine Learning module of my Computer Science Degree_

## Example
Examples / Documentation  found [here](/docs/Examples.ipynb)

![Example](https://github.com/edf1101/GradientDescent/assets/96292907/b8157a76-769f-4313-ad71-fcc6e20e574b)

- The blue points are the random points that somewhat fit the curve 2x<sup>2</sup> - 3x + 4
- The Red line is the actual curve
- The Green line is the predicted curve

## Info
Modules Used
- Matplotlib (if you want to visualise)
- Random (If you want to create random set of training data / train-test-split)

### Learning Parameters (for OK results)
- Quartic - learning = 0.0000000003
- Cubic - learning = 0.00000003
- Quadratic - learning = 0.000001
- Linear - learning = 0.00001

In general for each extra polynomial term you add it should be ~100x smaller.
Smaller learning rates may get better results, but you will need to have more attempts to reach it since it learns slower
