from custom_types import Corpus


class TargetVocabularySizeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class BPE:
    """Byte pair encoding tokenizer"""

    def calculate_frequency(self, words: list[str]) -> Corpus:
        """
        Calculates the frequency of each word in a list of words provided.

        Takes a list of words stored as strings and return a list of tuples where each tuple contains a string from the word list, an integer representing its frequency in the list.

        Args:
            Words (list): A list of strings, no order necessary.

        Returns:
            Corpus (list[tuple(str, int)]): A list of tuples where the first element is a string of a word in the word list and the second element is an integer representing the frequency of the word in the list.
        """
        umap = {}
        for word in words:
            if word in umap:
                umap[word] += 1
            else:
                umap[word] = 1

        corpus = Corpus([(word, umap[word]) for word in umap.keys()])
        return corpus

    def create_vocabulary(self, words: list[str]) -> list:
        """
        Creates a list of characters in the list of words.

        Args:
            Words (list): A list of strings, no order necessary.

            Returns:
                vocabulary (list), a list of characters used in the list of words provided.
        """
        return list(set("".join(words)))

    def find_pair_frequencies(self, corpus: Corpus) -> dict:
        """
        Finds the frequency of pairs of characters in the corpus and returns a dict.

        Args:
            (list[tuple(str, int)]): A list of tuples where the first element is a string of a word in the word list and the second element is an integer representing the frequency of the word in the list.
        Returns:
            dict of pair frequencies
        """
        pair_frequency_dict = {}

        for word, frequency in corpus:
            for i in range(len(word) - 1):
                char_pair = f"{word[i]}{word[i+1]}"
                if char_pair not in pair_frequency_dict:
                    pair_frequency_dict[char_pair] = frequency
                else:
                    pair_frequency_dict[char_pair] += frequency
        return pair_frequency_dict


if __name__ == "__main__":
    abc = ["apple", "mango", "banana", "banana", "banana", "banana", "mango", "mango"]
    tokenizer = BPE()
    corpus = tokenizer.calculate_frequency(abc)
    print(tokenizer.create_vocabulary(abc))
    print(tokenizer.count_pair_frequencies(corpus))
