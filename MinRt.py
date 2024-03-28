import os

import numpy as np


class MinRt:
    def __init__(self):
        raise NotImplementedError("This is a static class")

    @staticmethod
    def do_ai(input_array: np.ndarray, script: list[str]) -> int:
        current = np.array(input_array)
        # current = input_array.copy()
        # Dense layer
        if not os.path.exists('D1.npy'):
            raise RuntimeError("D1.npy No exist")

        weights = np.load('D1.npy')
        current = np.dot(current.reshape(1, -1), weights).flatten()

        # LeakyRelu layer
        n = 20
        if current.shape[0] != n:
            raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {current.shape[0]})")
        # Apply LeakyReLU function
        current = np.where(current > 0, current, current * 0.01)

        # Dense layer
        if not os.path.exists('D2.npy'):
            raise RuntimeError("D2.npy No exist")
        weights = np.load('D2.npy')
        current = np.dot(current.reshape(1, -1), weights).flatten()

        # LeakyRelu layer
        n = 100
        if current.shape[0] != n:
            raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {current.shape[0]})")
        # Apply LeakyReLU function
        current = np.where(current > 0, current, current * 0.01)


        # Dense layer
        if not os.path.exists('D3.npy'):
            raise RuntimeError("D3.npy No exist")
        weights = np.load('D3.npy')
        current = np.dot(current.reshape(1, -1), weights).flatten()

        # Judge layer
        m = 2
        if current.shape[0] != m:
            raise RuntimeError(f"Wrong input size for Judge layer (expected {m}, got {current.shape[0]})")
        # Find the index of the maximum value
        idx = np.argmax(current)
        return idx
