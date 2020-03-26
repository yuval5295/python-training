Sentence = raw_input('Wrihe somthing\n')
if 'a' in Sentence:
    Sentence=(Sentence.replace('a', 'aba'))
if 'e' in Sentence:
    Sentence=(Sentence.replace('e', 'ebe'))
if 'i' in Sentence:
    Sentence=(Sentence.replace('i', 'ibi'))
if 'o' in Sentence:
    Sentence=(Sentence.replace('o', 'obo'))
if 'u' in Sentence:
    Sentence=(Sentence.replace('u', 'ubu'))
print(Sentence)