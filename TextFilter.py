from typing import List
import os
from Tokenizer import Tokenizer
from MinRt import MinRt


class TextFilter:
    script: List[str]
    tokenizer: Tokenizer

    def __init__(self):
        self.tokenizer = Tokenizer("tokenize.model")

    def is_illegal(self, text: str) -> bool:
        # Assuming MinRt class and its do_ai method are defined in Python  
        return MinRt.do_ai(self.tokenizer.tokenize(text)) == 1
