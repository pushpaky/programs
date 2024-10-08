import random

words = (
    "which",
    "there",
    "their",
    "about",
    "would",
    "these",
    "other",
    "words",
    "could",
    "write",
    "first",
    "water",
    "after",
    "where",
    "right",
    "think",
    "three",
    "years",
    "place",
    "sound",
    "great",
    "again",
)


def isword(user_word, wordly_word):
    for x in user_word:
        print(x, end=" ")
    print()
    # If alphabet present in same position green
    # if alphabet present in word yellow
    # if alphabet is not present black
    for i in range(len(user_word)):
        if user_word[i] == wordly_word[i]:
            print("????", end="")
        elif user_word[i] in wordly_word:
            print("????", end="")
        else:
            print("⬛", end="")

    # if word present return true else return false
    if user_word == wordly_word:
        return 1
    else:
        return 0


random_word = random.choice(words)
print(random_word)
print("Let's Play Wordle")
message, i = {
    0: "Marvellous",
    1: "Excellent",
    2: "Very good",
    3: "Nice",
    4: "Good",
    5: "Ok",
}, 6
while i > 0:
    user_word = input("\nEnter word: ")
    if len(user_word) == 5 and user_word.isalpha():
        i = i - 1
        if isword(user_word, random_word):
            print("\n", message[i])
            break
        else:
            continue
    else:
        print("Please enter a valid word")
else:
    print("End of Game, the correct word is:", random_word)
