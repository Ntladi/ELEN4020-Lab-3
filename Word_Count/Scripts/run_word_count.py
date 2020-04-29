import os
import sys
import time

fileName = sys.argv[1]

startTime = time.time()
os.system("python3 word_count.py ../Input/" + fileName + " ../Output/")
endTime = time.time()
totalTime = (endTime - startTime)

file = open("../Output/source_0_split_0_.mtxt", "r")
output = open("../Output/word_count_output.txt","w")
output.write("The process took " + str(totalTime) + " seconds\n")
words = file.readlines()
for word in words:
	output.write(str(word))

file.close()
output.close()
os.system("rm ../Output/source_0_split_0_.mtxt")
print("Word count complete.")