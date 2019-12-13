import random

def convertToList(file):
    wordInput = []
    inputText = file.readlines()
    for line in inputText:
        for word in line.split(' '):
            if not word.isspace():
                wordInput.append(word.rstrip())
    return wordInput

def convertToMarkovChain(wordInput):
    markovChain = {}
    for i,word in enumerate(wordInput):
        key = word + ' ' + wordInput[i+1]
        try:
            if key in markovChain:
                markovChain[key].append(wordInput[i+2])
            else:
                markovChain[key] = [wordInput[i+2]]
        except Exception:
            break
    return markovChain

def naturalLanguageGeneration(wordInput, markovChain):
    textOutput = [wordInput[0], wordInput[1]]
    while len(textOutput) <= 500:
        key = textOutput[len(textOutput)-2] + ' ' + textOutput[len(textOutput)-1]
        if key in markovChain:
            textOutput.append(random.choice(markovChain[key]))
        else:
            break
    return textOutput

def outputText(textOutput):
    print()
    for word in textOutput:
        print(word, end=' ')
    print()
    fileOutput = input('Please enter an output filename: ')
    if len(fileOutput):
        outputFile = open(fileOutput,'w')
        currentLine = ''
        for word in textOutput:
            if len(currentLine) + len(word) <= 80:
                currentLine += word + ' '
            else:
                outputFile.write(currentLine+'\n')
                currentLine = word + ' '

while True:
    try:
        file = open(input('Please enter a filename:'),'r')
    except Exception:
        print('An error occurred')
        continue
    if file:
        break

wordInput = convertToList(file)
markovChain = convertToMarkovChain(wordInput)
textOutput = naturalLanguageGeneration(wordInput,markovChain)
outputText(textOutput)