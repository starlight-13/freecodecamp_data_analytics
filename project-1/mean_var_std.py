''' starlight13 '''
import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(nums).reshape(3, 3)

    def to_list(x):
        if isinstance(x, np.ndarray):
            return x.tolist()
        elif isinstance(x, np.generic):  # numpy scalar
            return x.item()
        return x

    calculations = {
        'mean': [
            to_list(matrix.mean(axis=0)),  # axis=0 => col-wise
            to_list(matrix.mean(axis=1)),  # row-wise
            to_list(matrix.mean())  # flattened
        ],
        'variance': [
            to_list(matrix.var(axis=0)),
            to_list(matrix.var(axis=1)),
            to_list(matrix.var())
        ],
        'standard_deviation': [
            to_list(matrix.std(axis=0)),
            to_list(matrix.std(axis=1)),
            to_list(matrix.std())
        ],
        'maximum_element': [
            to_list(matrix.max(axis=0)),
            to_list(matrix.max(axis=1)),
            to_list(matrix.max())
        ],
        'minimum_element': [
            to_list(matrix.min(axis=0)),
            to_list(matrix.min(axis=1)),
            to_list(matrix.min())
        ],
        'total_sum': [
            to_list(matrix.sum(axis=0)),
            to_list(matrix.sum(axis=1)),
            to_list(matrix.sum())
        ]
    }

    return calculations
