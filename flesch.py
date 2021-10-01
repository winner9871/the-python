"""
This program calculate and display Flesch index of writting inputted throug a
file
"""
import os

# Constants Defination
VOWELS = ("a", "e", "i", "o", "u")
SYLLABLE_END_EXCEPTIONS = ("es", "ed")

while True:
    fname = input("Enter the file whose flesch index to be calculate :\t")
    if os.path.exists(fname):
        break
    else:
        print(f"{fname} doesn't exists please enter a valid file name")

with open(fname , "rt") as fobj:
    content = fobj.read()

# Getting the sentances from content
sentences = content.replace(".", "#Sentence Ended Here#")
sentences = sentences.replace("?", "#Sentence Ended Here#")
sentences = sentences.replace("!", "#Sentence Ended Here#")
sentences = sentences.replace(":", "#Sentence Ended Here#")
sentences = sentences.replace(";", "#Sentence Ended Here#")
sentences = sentences.split("#Sentence Ended Here#") 

# Getting Words from sentances
words = []
for sentence in sentences: words += sentence.split()

# Getting Syllable from words
syllablesCount = 0
for word in words:
    for vowel in VOWELS:
        syllablesCount += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllablesCount -= 1
    if word.endswith('le'):
        syllablesCount += 1

# Counters
wordCount = len(words)
sentencesCount = len(sentences)
# syllablesCount defined at line 34

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (wordCount / sentencesCount) - \
        84.6 * (syllablesCount / wordCount)
level = round(0.39 * (wordCount / sentencesCount) + 11.8 * \
        (syllablesCount / wordCount) - 15.59)
# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(len(sentences), "sentences")
print(len(words), "words")
print(syllablesCount, "syllables")

