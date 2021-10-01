import random
# Vocabulary: words in 4 different parts of speech
ARTICLE = ("A", "THE")
NOUN = ("BOY", "GIRL", "BAT", "BALL")
VERB = ("HIT", "SAW", "LIKED")
PREPOSITION = ("WITH", "BY")

def sentence():
    """Builds and return sentence"""
    return " ".join((nounPhase(), verbPhase()))
def verbPhase():
    """Builds and return verb phase"""
    return " ".join((random.choice(VERB), nounPhase(), prepositionPhase()))
def prepositionPhase():
    """Builds and return preposition phase"""
    return " ".join((random.choice(PREPOSITION), nounPhase()))
def nounPhase():
    """Builds and return noun phase"""
    return " ".join((random.choice(ARTICLE), random.choice(NOUN)))

def main():
    print("Anytime Enter 0 to exit")
    while True:
        sentenceCount = int(input("How many sentences you want :\t"))
        if sentenceCount == 0:
            break
        for _ in range(sentenceCount):
            print(sentence())

if __name__ == "__main__":
    main()

