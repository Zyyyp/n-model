import os
import argparse
import numpy as np
import pickle
getall = argparse.ArgumentParser()

getall.add_argument("--input-dir", dest="trainPath",default = 'C:\\Users\\HP\\Desktop\\цепь маркова\\data',  type=str)
getall.add_argument("--model", dest="resultPath", default='C:\\Users\\HP\\Desktop\\цепь маркова\\model')
inputt= getall.parse_args()
os.chdir(inputt.trainPath)
allfiles = os.listdir()
model={}
writer=[]
def writevalue(key,nextKey):
    if key in model:
        if nextKey in model[key]:
            model[key][nextKey]+=1
            model[key]['evrythingyoucanimagine']+=1
        else:
            model[key][nextKey]=1
            model[key]['evrythingyoucanimagine']+=1
    else:
        model[key]={nextKey:1, 'evrythingyoucanimagine':1}
for file in allfiles:
    with open(file, "r") as f:
        a = f.read()
    a=np.array(a.split('\n'))
    s=np.array([])
    for i in range(len(a)):
        s = np.concatenate((s,a[i].split(' ')),axis=0)
        print(s)
    for i in range(len(s)-1):
        writer.append(s[i])
        writevalue(writer[len(writer)-1],s[i+1])
        if len(writer)>=2:
            writevalue(writer[len(writer)-2]+' '+writer[len(writer)-1],s[i+1])
        if len(writer)>=3:
            writevalue(writer[0]+' '+writer[1]+' '+writer[2],s[i+1])
            writer.pop(0)
    print(model)
    f.close()
with open (inputt.resultPath,'wb') as q:
    pickle.dump(model,q)
q.close()
#print(os.listdir())