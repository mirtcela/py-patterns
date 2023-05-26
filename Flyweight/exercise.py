class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self.formatted_words = {}
        
    class WordFormat:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize
    
    def __getitem__(self, idx):
        wt = self.WordFormat()
        self.formatted_words[idx] = wt
        return self.formatted_words[idx]
    
    def __str__(self):
        result = []
        for i in range(len(self.words)):
            w = self.words[i]
            if i in self.formatted_words and self.formatted_words[i].capitalize:
                w = w.upper()
            result.append(w)
        return ' '.join(result)
    
def main():
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)

main()