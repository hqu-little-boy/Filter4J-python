import numpy as np
class Tokenizer:
    def __init__(self):
        self.vocab = None

    def __init__(self, filename):
        try:
            with open(filename, 'r', encoding='utf8') as file:
                size = int(file.readline().strip())
                self.vocab = [file.readline().strip() for _ in range(size)]
            # return Tokenizer(vocab)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def tokenize(self, text):
        if self.vocab is None:
            raise ValueError("Tokenizer not initialized with a vocabulary.")
        values = [1 if word in text else 0 for word in self.vocab]
        return values
