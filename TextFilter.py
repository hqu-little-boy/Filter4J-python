from typing import List
import os
from Tokenizer import Tokenizer
from MinRt import MinRt


class TextFilter:
    script: List[str]
    tokenizer: Tokenizer

    def __init__(self):
        if not os.path.exists("judge.model") or not os.path.exists("tokenize.model"):
            raise FileNotFoundError("Both 'judge.model' and 'tokenize.model' files are required.")

        with open("judge.model", 'r', encoding='utf8') as file:
            self.script = [line.strip() for line in file]

        self.tokenizer = Tokenizer("tokenize.model")

    def is_illegal(self, text: str) -> bool:
        # Assuming MinRt class and its do_ai method are defined in Python  
        return MinRt.do_ai(self.tokenizer.tokenize(text), self.script) == 1
