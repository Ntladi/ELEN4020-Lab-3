import sys
import shutil, os
import time

inputFile = sys.argv[1]
outputFile = sys.argv[2]

def get_key_and_line_numbers(wordData):
	firstBracket = wordData.find("(")
	lastBracket = wordData.find(")")
	wordData = wordData[firstBracket + 1:lastBracket]
	word,lineNumbers = wordData.split(",",1)
	return word,lineNumbers

if (os.path.isdir("./Temp/")):
    os.system("rm -rf ./Temp/")
	
wordsWithLineNumbers = []
startTime = time.time()	
os.system("python3 ./Scripts/inverted_index.py "  + inputFile + " ./Temp/")
file = open("Temp/source_0_split_0_.mtxt", "r")
output = open(outputFile,"w")

words = file.readlines()
for wordData in words:
	word,lineNumbers = get_key_and_line_numbers(wordData)
	wordsWithLineNumbers.append([word,lineNumbers])

endTime = time.time()
totalTime = (endTime - startTime)
output.write("The process took " + str(totalTime) + " seconds\n")
for distinct_word in wordsWithLineNumbers[:50]:
	output.write(distinct_word[0] + " " + distinct_word[1] + "\n")

file.close()
output.close()