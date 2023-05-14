import pandas as pd # Pandas to deal with CSV files

def convTuples(letterDict): # Function to convert dictionary with list to dictionary with tuples
    for i in letterDict:
        letterDict[i] = tuple(letterDict[i])
    return letterDict

def readstats(): # Reads csv file, parses through and converts to dictionary with lists to dictionary with tuples and returns it
    data = pd.read_csv("letterFrequency.csv")
    letterDict = data.set_index('Unnamed: 0').T.to_dict('list')
    letterDict = convTuples(letterDict)
    return letterDict

def createRank(data,letterDict): # Function to rank the words
    wordDict = {}
    for i in data: # Create likelihood values
        temp = 1
        for j in range(len(i)):
            temp = temp * letterDict[i[j]][j]
        wordDict[i] = temp / (len(data)**5)

    wordDict = sorted(wordDict.items(), key=lambda x:x[1], reverse = True) # Sort the dictionary in descending order
    wordList = []
    likelihood = []
    for i in wordDict:
        wordList.append(i[0])
        likelihood.append(i[1])
    
    temp = {"Word":wordList,"Likelihood":likelihood} # Dictionary to create dataframe
    dataFrame = pd.DataFrame(data = temp, index = list(range(1,len(data)+1)))
    dataFrame = dataFrame[:-1] # Removing the last value which is empty from 5Letter.txt
    dataFrame.to_csv("wordRank.csv") # Saving to csv

def main():
    f = open("5Letter.txt","r") # work on words with only 5 letters
    data = f.read().split("\n")

    letterDict = {"A":[0,0,0,0,0],"B":[0,0,0,0,0],"C":[0,0,0,0,0],"D":[0,0,0,0,0],"E":[0,0,0,0,0],"F":[0,0,0,0,0],"G":[0,0,0,0,0],"H":[0,0,0,0,0],"I":[0,0,0,0,0],"J":[0,0,0,0,0],"K":[0,0,0,0,0],"L":[0,0,0,0,0],"M":[0,0,0,0,0],"N":[0,0,0,0,0],"O":[0,0,0,0,0],"P":[0,0,0,0,0],"Q":[0,0,0,0,0],"R":[0,0,0,0,0],"S":[0,0,0,0,0],"T":[0,0,0,0,0],"U":[0,0,0,0,0],"V":[0,0,0,0,0],"W":[0,0,0,0,0],"X":[0,0,0,0,0],"Y":[0,0,0,0,0],"Z":[0,0,0,0,0]}

    for i in data: # Parse through words and add occurences
        for j in range(len(i)):
            letterDict[i[j]][j] = letterDict[i[j]][j] + 1


    temp = [] # Take values into a list for converting to dataframe
    for i in letterDict.values():
        temp.append(i)

    dataFrame = pd.DataFrame(data = temp, columns=['Position 1', 'Position 2','Position 3','Position 4','Position 5'], index = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) # Making the dataframe
    dataFrame = dataFrame.div(len(data)) # Converting into percentage
    dataFrame = dataFrame.round(4) # Rounding off to 4 decimal places
    dataFrame.to_csv("letterFrequency.csv") # Saving to csv

    createRank(data,letterDict)
    f.close() # Closing the file
    return len(data)


if __name__ == "__main__":
    main()