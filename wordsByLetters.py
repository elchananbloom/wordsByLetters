import copy
import enchant

#@author Elchanan

# combine two lists to a new list of all possible combinations
def combineTwoLists(l, list):
    return [x + y for x in l for y in list]

#in given list of letters the function prints all possible combinations of the letters
# that is in the english dictionary
def findWords(l):
    #get the english dictionary
    enDict = enchant.Dict("en_US")
    allWords = copy.deepcopy(l)

    #combine all the possible combinations
    for i in range(len(l) - 1):
        allWords += combineTwoLists(l, allWords)
    #order and removes dobble words
    allWords = set(allWords)
    #take only words in the english dictionary that is up than 2 letters
    wordsInDict = list(filter(lambda x: len(x) > 2 and enDict.check(x), allWords))

    print(len(wordsInDict), " words found")
    #print all possible combination of the letters in upper letter
    #by sort it by their length and then alphabetically
    print(sorted([x.upper() for x in wordsInDict], key=lambda x:(len(x),x)))


def main():
    l = input("Enter the letters: ")
    findWords(list(l))


if __name__ == '__main__':
    main()
