# Gradient Descent Module

Gradient Descent module written by https://github.com/edf1101/ for my University Computer Science Degree

## Info
Modules Used
- Matplotlib (if you want to visualise)
- Random (If you want to create random set of training data / train-test-split)

### Learning Parameters (for OK results)
- Quartic - learning = 0.0000000003
- Cubic - learning = 0.00000003
- Quadratic - learning = 0.000001
- Linear - learning = 0.0003

In general for each extra polynomial term you add it should be ~100x smaller.
Smaller learning rates may get better results, but you will need to have more attempts to reach it since it learns slower
