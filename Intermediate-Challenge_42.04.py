import random

import pickle, shelve

scoreFile = open("scoreFile2.dat", "wb")

randomlist = []
for i in range(0,200):
   n = random.randint(1,1000)
   randomlist.append(n)

pickle.dump(randomlist, scoreFile)
scoreFile.close()
scoreFile2 = open("scoreFile2.dat","rb")
readWords = pickle.load(scoreFile2)
readWords = sorted(readWords)
print(readWords)


userInput = int(input("What was your time in the race, in seconds?" ))

for i in range(len(readWords)):

   if userInput <= readWords[i]:
      print(i+1)

      break
