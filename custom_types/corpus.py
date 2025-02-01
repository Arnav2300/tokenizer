from typing import List, Tuple


class Corpus:
    def __init__(self, data: List[Tuple[str, int]]):
        """
        Initializes the Corpus with a list of word-freqeuncy tuples.
        """
        self.data = data

    def add(self, word: str, frequency: int):
        """
        Adds a new word-frequency pair to the Corpus.
        """
        self.data.append((word, frequency))

    def get(self, word: str) -> int:
        """
        Gets the frequency of a word in the corpus.
        """
        for w, freq in self.data:
            if w == word:
                return freq
        return 0  # Return 0 if the word is not found

    def __repr__(self):
        return f"Corpus({self.data})"

    def to_dict(self):
        """
        Converts Corpus to a dictionary.
        """
        return dict(self.data)
