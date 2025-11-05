# Função para inverter as palavras
def invert_words(sentence):
    words = sentence.split()
    inverted_words = [word[::-1] for word in words]
    return ' '.join(inverted_words)

input_sentence = input("Escreva uma frase ou palavra: ")
result = invert_words(input_sentence)
print(result)
