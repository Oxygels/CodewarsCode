from itertools import cycle

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        res = []
        text = list(map(ord,text))
        for (i,k) in enumerate(cycle(self.key)):
            if i == len(text): break
            if chr(text[i]) not in self.alphabet: 
                res.append(chr(text[i]))
                continue
            
            value = ((text[i] - 97 + ord(k) - 97) % 26) + 97
            res.append(chr(value))
        return "".join(res)
    
    def decode(self, text):
        res = []
        text = list(map(ord,text))
        for (i,k) in enumerate(cycle(self.key)):
            if i == len(text): break
            if chr(text[i]) not in self.alphabet: 
                res.append(chr(text[i]))
                continue
            
            value = ((text[i] - 97 - (ord(k) - 97)) % 26) + 97
            print(text)
            res.append(chr(value))
        return "".join(res)

