import os
import argparse
import numpy as np
import pickle
import random as rd
getall = argparse.ArgumentParser()

getall.add_argument("--prefix", dest="prefix",default = 'dfghkjl;ogfdxvb',  type=str)
getall.add_argument("--model", dest="modelPath", default='C:\\Users\\HP\\Desktop\\цепь маркова\\model')
getall.add_argument("--length", dest="lenght", default=7)
inputt= getall.parse_args()
with open(inputt.modelPath, 'rb') as f:
    model = pickle.load(f)
f.close()
def getNext(lastWords):
    if lastWords in model:
        random = rd.randint(1,model[lastWords]['evrythingyoucanimagine'])
        for i in model[lastWords].keys():
            if random <= model[lastWords][i]:
                return i
                break
            else:
                random-=model[lastWords][i]
    else:
        if len(lastWords)==1:
            return model[model.keys()[0]]
        else:
            return '-1'
originalPrefix = inputt.prefix
allInput = inputt.prefix.split(' ')
inputLen = len(allInput)
randomChance = 1
if inputLen<=3:
    lastWords=allInput
else:
    lastWords = [allinput[inputLen-3],allinput[inputLen-2],allinput[inputLen-1]]
for i in range(inputt.lenght):
    if len(lastWords)==1:
        originalPrefix = originalPrefix+' ' + getNext(lastWords[0])
        lastWords.append(getNext(lastWords[0]))
    elif len(lastWords)==2:
        newWord=getNext(lastWords[0]+' '+lastWords[1])
        if newWord=='-1':
            newWord=getNext(lastWords[1])
        originalPrefix = originalPrefix+' ' + newWord
        lastWords.append(newWord)
    else:
        chance=rd.randint(1,100)
        newWord = getNext(lastWords[0]+' '+lastWords[1]+' ' +lastWords[2])
        if newWord=='-1' or chance<=randomChance:
            randomChance=1
            newWord = getNext(lastWords[1]+' '+lastWords[2])
            if newWord=='-1':
                newWord = getNext(lastWords[2])
        else:
            randomChance *=2
        originalPrefix = originalPrefix+' ' + newWord
        lastWords.append(newWord)
        lastWords.pop(0)
        
print(originalPrefix)
        
    