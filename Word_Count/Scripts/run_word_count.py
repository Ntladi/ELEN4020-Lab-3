import os
import sys
import time

inputFile = sys.argv[1]
outputFile = sys.argv[2]

startTime = time.time()
os.system("python3 ./Scripts/word_count.py " + inputFile + " ./Temp/")
endTime = time.time()
totalTime = (endTime - startTime)

file = open("./Temp/source_0_split_0_.mtxt", "r")
output = open(outputFile,"w")
output.write("The process took " + str(totalTime) + " seconds\n")
words = file.readlines()
for word in words:
	output.write(str(word))

file.close()
output.close()
