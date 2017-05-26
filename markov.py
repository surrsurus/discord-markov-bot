import random

# Inspired by https://gist.githubusercontent.com/agiliq/131679/raw/33ff96bbb536b71e989276d9f7a728037b124048/gistfile1.py

class Markov(object):

    def __init__(self):
        # Since we split on whitespace, this can never be a word
        self.stopword = "\n"

        # Cause a "new sentence" if found at the end of a word
        self.stopsentence = (".", "!", "?", "\n")

        # Table of markov chains
        self.table = {}

    def addToTable(self, sentence):
        w1 = self.stopword
        w2 = self.stopword

        for word in sentence.split():

            if word[-1] in self.stopsentence:
                self.table.setdefault( (w1, w2), [] ).append(word[0:-1])
                w1, w2 = w2, word[0:-1]
                word = word[-1]

            self.table.setdefault( (w1, w2), [] ).append(word)
            w1, w2 = w2, word

        self.table.setdefault( (w1, w2), [] ).append(self.stopword)

    def generate(self, maxSen=7):
        try:

            w1 = self.stopword
            w2 = self.stopword
            sentencecount = 0
            sentence = []

            while sentencecount < maxSen:

                newword = random.choice(self.table[(w1, w2)])

                if newword == self.stopword:
                    w1, w2 = w2, newword
                if newword in self.stopsentence:
                    sentencecount += 1
                else:
                    sentence.append(newword)

                w1, w2 = w2, newword

            final = ' '.join(sentence).replace('\n', '')

            if len(final) > 2000:
                return self.generate()
            else:
                return final

        except Exception as e:
            print(e)
            return "Not enough data!"
