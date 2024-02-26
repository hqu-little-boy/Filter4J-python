from typing import List


class MinRt:
    def __init__(self):
        raise NotImplementedError("This is a static class")

    @staticmethod
    def do_ai(input: List[float], script: List[str]) -> int:
        current = input.copy()

        for str_layer in script:
            if len(str_layer) < 2:
                continue

            tokens = str_layer.split(" ")

            layer_type = tokens[0]

            if layer_type == "D":  # Dense layer
                ic = int(tokens[1])
                oc = int(tokens[2])

                if len(current) != ic:
                    raise RuntimeError(f"Wrong input size for Dense layer (expected {ic}, got {len(current)})")

                tmp = [0.0] * oc
                for i in range(oc):
                    sum_ = 0.0
                    for j in range(ic):
                        sum_ += current[j] * float(tokens[3 + i + j * oc])
                    tmp[i] = sum_

                current = tmp

            elif layer_type == "L":  # LeakyRelu layer
                n = int(tokens[1])

                if len(current) != n:
                    raise RuntimeError(f"Wrong input size for LeakyRelu layer (expected {n}, got {len(current)})")

                for i in range(n):
                    current[i] = current[i] if current[i] > 0 else current[i] * 0.01

            elif layer_type == "J":  # Judge layer
                m = int(tokens[1])

                if len(current) != m:
                    raise RuntimeError(f"Wrong input size for Judge layer (expected {m}, got {len(current)})")

                idx = 0
                for i in range(1, m):
                    if current[i] > current[idx]:
                        idx = i

                return idx

            else:
                raise RuntimeError("Unknown layer type")

        raise RuntimeError("No output layer")