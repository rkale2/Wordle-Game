import random


class Wordle:  # When playing wordle manually

    solution = []
    attemptList = ["None"]
    attempts = 6
    wordList = []

    def __init__(self):  # Intialize the wordle game with a random word
        f = open("5Letter.txt")
        words = f.read().split("\n")

        self.wordList = words
        self.solution = list(words[random.randint(0, 5758)].upper())

    def __str__(self):  # Print current state of wordle game
        attemptsMade = ",".join(self.attemptList)
        return 'Solution is ' + "".join(self.solution) + ' number of attempts remaining is ' + str(self.attempts) + ' and words attempted till now are ' + attemptsMade

    def intro(self):  # Quick introduction of the game
        print()
        print("Welcome to wordle")
        print()
        print("Correct letters in correct positions will have a '+' under them, correct letters in incorrect positions will have a '*' under them and incorrect letters will have '-' under them.")
        print("You will have 6 guesses.")
        print()

    def loss(self):  # Runs of the player loses
        print()
        print("Sorry you have run out of attempts. You lose, the word was " +
              "".join(self.solution))

    def input(self):  # Check inputs and add to attemptlist
        while True:
            temp = input()
            temp = list(temp.upper())
            if len(temp) != 5:
                print()
                print("Word length is not 5")
                print()
                continue
            elif "".join(temp) in self.attemptList:
                print()
                print("Word has already been tried")
                print()
                continue
            elif not "".join(temp).isalpha():
                print()
                print("Word has non alphabetic characters")
                print()
                continue
            elif "".join(temp) not in self.wordList:
                print()
                print("Word doesn't exist")
                print()
                continue
            else:
                self.attemptList.append("".join(temp))
                return temp

    def checkWord(self, currentAttempt):  # Generate result for user input

        flag = 0  # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
        result = ["", "", "", "",
                  ""]  # Assigns " ",""" or "'" depending on correct and incorrect letters and positions
        search = ["0", "0", "0", "0",
                  "0"]  # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
        pos = 0  # Used to track the letter that is being used in the actual word to create result

        # Checking for correct letters in correct positions first, to ensure highest priority
        for i in range(5):
            if(currentAttempt[i] == self.solution[i]):
                flag = flag + 1
                result[i] = ("+")
                search[i] = 1

        # Checking for correct letters in incorrect position and lastly incorrect letters
        for i in range(5):
            if(currentAttempt[i] in self.solution and result[i] == ""):
                pos = "".join(self.solution).find(currentAttempt[i])
                if(search[pos] == 1):
                    result[i] = ("-")
                else:
                    result[i] = ("*")
                    search[pos] = 1
            elif result[i] == "":
                result[i] = ("-")

        return (result, flag)

    def win(self):  # Runs if user wins
        print()
        print("Congratulations you have guessed the right word!")
        print()


if __name__ == "__main__":  # Play game by user
    w = Wordle()
    w.intro()
    # Uncomment next line to turn on debugger
    # print(w.__str__())
    while w.attempts > 0:
        print()
        print("Please make your " + str(7 - w.attempts) + " guess")
        currentAttempt = w.input()
        result, flag = w.checkWord(currentAttempt)

        if flag == 5:
            w.win()
            break

        for i in range(5):
            print(result[i], end="")
        print()

        w.attempts -= 1
    else:
        w.loss()


def play(solution, guess):  # Used by solver
    w = Wordle()
    w.solution = solution
    currentAttempt = list(guess)
    return w.checkWord(currentAttempt)
