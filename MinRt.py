# class MinRt:
#     def __init__(self):
#         raise NotImplementedError("This is a static class")
#
#     @staticmethod
#     def do_ai(input: list[float], script: list[str]) -> int:
#         current = input.copy()
#
#         for str_layer in script:
#             if len(str_layer) < 2:
#                 continue
#
#             tokens = str_layer.split(" ")
#
#             layer_type = tokens[0]
#
#             if layer_type == "D":  # Dense layer
#                 ic = int(tokens[1])
#                 oc = int(tokens[2])
#
#                 if len(current) != ic:
#                     raise RuntimeError(f"Wrong input size for Dense layer (expected {ic}, got {len(current)})")
#
#                 tmp = [0.0] * oc
#                 for i in range(oc):
#                     sum_ = 0.0
#                     for j in range(ic):
#                         sum_ += current[j] * float(tokens[3 + i + j * oc])
#                     tmp[i] = sum_
#                 current = tmp
#
#             elif layer_type == "L":  # LeakyRelu layer
#                 n = int(tokens[1])
#
#                 if len(current) != n:
#                     raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {len(current)})")
#
#                 for i in range(n):
#                     current[i] = current[i] if current[i] > 0 else current[i] * 0.01
#             elif layer_type == "J":  # Judge layer
#                 m = int(tokens[1])
#
#                 if len(current) != m:
#                     raise RuntimeError(f"Wrong input size for Judge layer (expected {m}, got {len(current)})")
#
#                 idx = 0
#                 for i in range(1, m):
#                     if current[i] > current[idx]:
#                         idx = i
#                 return idx
#
#             else:
#                 raise RuntimeError("Unknown layer type")
#
#         raise RuntimeError("No output layer")

import numpy as np


class MinRt:
    def __init__(self):
        raise NotImplementedError("This is a static class")

    @staticmethod
    def do_ai(input_array: np.ndarray, script: list[str]) -> int:
        current = np.array(input_array)
        # current = input_array.copy()
        for str_layer in script:
            tokens = str_layer.split(" ")

            layer_type = tokens[0]

            if layer_type == "D1":  # Dense layer
                weights = np.load('D1.npy')
                current = np.dot(current.reshape(1, -1), weights).flatten()

            elif layer_type == "D2":  # Dense layer
                weights = np.load('D2.npy')
                current = np.dot(current.reshape(1, -1), weights).flatten()

            elif layer_type == "D3":  # Dense layer
                weights = np.load('D3.npy')
                current = np.dot(current.reshape(1, -1), weights).flatten()

            elif layer_type == "L1":  # LeakyRelu layer
                n = 20

                if current.shape[0] != n:
                    raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {current.shape[0]})")

                    # Apply LeakyReLU function
                current = np.where(current > 0, current, current * 0.01)

            elif layer_type == "L2":  # LeakyRelu layer
                n = 100

                if current.shape[0] != n:
                    raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {current.shape[0]})")

                    # Apply LeakyReLU function

                current = np.where(current > 0, current, current * 0.01)

            elif layer_type == "J":  # Judge layer
                m = 2

                if current.shape[0] != m:
                    raise RuntimeError(f"Wrong input size for Judge layer (expected {m}, got {current.shape[0]})")

                    # Find the index of the maximum value
                idx = np.argmax(current)

                return idx

            else:
                raise RuntimeError("Unknown layer type")

        raise RuntimeError("No output layer")
