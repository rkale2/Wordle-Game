import pandas as pd

class Node: # Node class
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print first 50 method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
  def print50(self):
    current = self.head
    count = 0
    while(current and count < 50):
      print(current.data)
      count = count + 1
      current = current.next


if __name__ == "__main__": # Runs if user uses helper
    print("Hello! This is the wordle helper.")
    print()
    print("Please enter the good letters or enter for no known good letters")
    while True: # Takes good letters
        goodLetters = input()
        if len(goodLetters)>5:
            print("You cannot have more than 5 goodLetters letters")
            continue
        if not (goodLetters.isalpha() or goodLetters == ""):
            print("You entered non alphabetic character")
            continue
        break
    goodLetters = goodLetters.upper()
    goodLetters = list(set(list(goodLetters)))
    
    print("Please enter bad letters or enter for no known bad letters")
    while True: # Takes bad letters
        badLetters = input()
        if not (badLetters.isalpha() or badLetters == ""):
            print("You entered non alphabetic character")
            continue
        break
    badLetters = badLetters.upper()
    badLetters = list(set(list(badLetters)))

  #  Takes all 5 letters if known
    print("Please enter any known characters in the word, put in a space for unknown letters or just press enter to move on.")
    while True:
        temp = input()
        if not (temp.isalpha() or temp == "" or len(temp) == 5):
            print("Please give proper inputs")
            continue
        break

    if temp == "":
        first = " "
        second = " "
        third = " "
        fourth = " "
        fifth = " "
    else:
        temp = list(temp)
        first = temp[0].upper()
        second = temp[1].upper()
        third = temp[2].upper()
        fourth = temp[3].upper()
        fifth = temp[4].upper()


    # generate wordlist and result linked list
    wordRank = pd.read_csv("wordRank.csv")
    wordList = list(wordRank["Word"])
    result = LinkedList()
    for i in wordList: # Generate result list based on goodLetters badLetters and known letters
        word = list(i)
        flag = 1
        if len(goodLetters) > 0:
            for j in goodLetters:
                if j not in word:
                    flag = 0
        if len(badLetters) > 0:
            for j in badLetters:
                if j in word:
                    flag = 0
        if first != " ":
            if word[0] != first:
                flag = 0
        if second != " ":
            if word[1] != second:
                flag = 0
        if third != " ":
            if word[2] != third:
                flag = 0
        if fourth != " ":
            if word[3] != fourth:
                flag = 0
        if fifth != " ":
            if word[4] != fifth:
                flag = 0
        if flag == 1:
            result.insert("".join(word))

    print("Top possible solutions to this wordle, are given below in order of likelihood.")
    result.print50() # Print first 50 letters


def printTop(prev="",goodLetters=[],badLetters=[],first="",second="",third="",fourth="",fifth=""): # Used by solver to play the game returns only first topmost word
    goodLetters = list(set(list(goodLetters)))

    badLetters = list(set(list(badLetters)))

    first = first.upper()
    second = second.upper()
    third = third.upper()
    fourth = fourth.upper()
    fifth = fifth.upper()


    wordRank = pd.read_csv("wordRank.csv")
    wordList = list(wordRank["Word"])
    for i in wordList:
        word = list(i)
        flag = 1
        if len(goodLetters) > 0:
            for j in goodLetters:
                if j not in word:
                    flag = 0
        if len(badLetters) > 0:
            for j in badLetters:
                if j in word:
                    flag = 0
        if len(first) > 0:
            if word[0] != first:
                flag = 0
        if len(second) > 0:
            if word[1] != second:
                flag = 0
        if len(third) > 0:
            if word[2] != third:
                flag = 0
        if len(fourth) > 0:
            if word[3] != fourth:
                flag = 0
        if len(fifth) > 0:
            if word[4] != fifth:
                flag = 0
        if flag == 1 and "".join(word) not in prev:
            return("".join(word))