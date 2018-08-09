def is_pangram(sentence):
    alfabet = list('abcdefghijklmnopqrstuvwxyz')
    return len(set(list(sentence.lower())).intersection(alfabet)) == 26
