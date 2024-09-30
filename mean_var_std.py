import numpy as np


def calculate(list):
    """Create a function named calculate() in mean_var_std.py that uses
    Numpy to output the mean, variance, standard deviation, max, min,
    and sum of the rows, columns, and elements in a 3 x 3 matrix.

    The input of the function should be a list containing 9 digits.
    The function should convert the list into a 3 x 3 Numpy array, and
    then return a dictionary containing the mean, variance, standard
    deviation, max, min, and sum along both axes and for the flattened
    matrix.

    The returned dictionary should follow this format:

    ```{
      'mean': [axis1, axis2, flattened],
      'variance': [axis1, axis2, flattened],
      'standard deviation': [axis1, axis2, flattened],
      'max': [axis1, axis2, flattened],
      'min': [axis1, axis2, flattened],
      'sum': [axis1, axis2, flattened]
    }```

        https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator
    """
    data = np.array(list)
    calculations = {
        "mean": [
            np.mean(data, axis=0),
            np.mean(data, axis=1),
            np.mean(data),
        ],
        "variance": [
            np.var(data, axis=0),
            np.var(data, axis=1),
            np.var(data),
        ],
        "standard deviation": [
            np.std(data, axis=0),
            np.std(data, axis=1),
            np.std(data),
        ],
        "max": [
            np.max(data, axis=0),
            np.max(data, axis=1),
            np.max(data),
        ],
        "min": [
            np.min(data, axis=0),
            np.min(data, axis=1),
            np.min(data),
        ],
        "sum": [
            np.sum(data, axis=0),
            np.sum(data, axis=1),
            np.sum(data),
        ],
    }

    return calculations
