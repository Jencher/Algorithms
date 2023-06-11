# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything

string1 = "Everything is hard before it is easy"

def reverse_statement(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

print(reverse_statement(string1))
