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
scoreFile2.close()
readWords = sorted(readWords)
print(readWords)


# Keep asking until the input is a whole number
while True:
   try:
      userInput = int(input("What was your time in the race, in seconds? "))
      break
   except ValueError:
      print("Please enter a whole number of seconds.")

# Slower than every racer means last place
placement = len(readWords) + 1

for i in range(len(readWords)):

   if userInput <= readWords[i]:
      placement = i+1

      break

print(placement)
