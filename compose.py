import os
import re
import string
import os
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as file:
        text = file.read()

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '',string.punctuation))

    words = text.split()

    words = words[:1000]

    return words

def make_graph(words):
    g = Graph()
    prev_word = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if prev_word:
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex;

        g.generate_probability_map()

        return g

def compose(g, words, length=50):
    compositions = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        compositions.append(word.value)
        word = g.get_next_word(word)

    return compositions

def main():
    words = get_words_from_text('texts/harry_potter.txt')

    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))

if __name__ == '__main__':
    main()