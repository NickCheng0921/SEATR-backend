import math

def calculate_grid_size(X):
    """
    Calculate the number of rows and columns for a grid large enough to hold X people.

    Args:
        X (int): Total number of people.

    Returns:
        tuple: Tuple of integers representing the size of the grid (rows, columns).
    """
    sqrt_X = math.ceil(math.sqrt(X))  # Round up square root of X to get the smallest integer greater than or equal to it
    N = sqrt_X  # Number of rows is equal to square root of X
    K = math.ceil(X / N)  # Number of columns is calculated as ceil(X / N)

    return N, K