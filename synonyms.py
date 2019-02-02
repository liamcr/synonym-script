from datamuse import datamuse
from random import randint

# Initialize variables
api = datamuse.Datamuse()
oldSentence = input("Enter a sentence: ")
listOfWords = oldSentence.split(" ")
isFeelingLucky = False
numSugs = 5
newSentence = ""

feelingLucky = input("Feeling lucky? (y/n) ")

if (feelingLucky == "y"):
    isFeelingLucky = True
    luckynessLevel = int(input(f"How lucky? (On a scale from 1 to {numSugs}) "))

for word in listOfWords:
    # Words that are less than 3 characters, are proper nouns, or the word 'the' don't seem to
    # produce great synonym options
    if len(word) <= 2 or word[0].isupper() or word == "the":
        newSentence += word + " "
        continue
    
    # Put the top synonym suggestions in a list
    synonyms = api.words(ml = word, max = numSugs)
    topSuggestions = [item['word'] for item in synonyms]

    replacementWord = word

    if len(topSuggestions) != 0:
        if (isFeelingLucky):
            if (len(topSuggestions) >= luckynessLevel):
                replacementWord = topSuggestions[randint(0, luckynessLevel - 1)]
            else:
                replacementWord = topSuggestions[randint(0, len(topSuggestions) - 1)]
        else:
            print(f"Enter a number to choose replacement word for {word}:")
            print("\t0: Don't replace")
            for i in range(0, len(topSuggestions)):
                print(f"\t{i + 1}: {topSuggestions[i]}")
            
            choice = int(input())

            if choice > 0:
                replacementWord = topSuggestions[choice - 1]
    elif (not isFeelingLucky):
        print(f"No synonym suggestions for {word}")


    newSentence += replacementWord
    
    newSentence += " "

print(newSentence)