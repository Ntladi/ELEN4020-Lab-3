import sys
import shutil, os
import time

inputFile = sys.argv[1]
outputFile = sys.argv[2]
indexes = sys.argv[3]
linesToCount = int(sys.argv[4])

def compare_by_occurence(wordsWithLineNumbers):
	# This function sorts a list in decending order
	return len(wordsWithLineNumbers[1].split(","))

def sort_words(wordsWithLineNumbers):
	# This method sorts the list of words in decending order and returns the result
	# as a key value pair
	allWordsWithLineNumbers = sorted(wordsWithLineNumbers, key = compare_by_occurence, reverse = True)
	return allWordsWithLineNumbers

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
allWordsWithLineNumbers = sort_words(wordsWithLineNumbers)
totalTime = (endTime - startTime)
output.write("The process (Including sorting the list) took" + str(totalTime) + " seconds\n")
output.write("The first " + str(linesToCount) + " line numbers of the top " + indexes + " words:\n")
for distinct_word in allWordsWithLineNumbers[:int(indexes)]:
	word = distinct_word[0]
	lines = distinct_word[1].split(",")
	length = linesToCount
	if (len(lines) < linesToCount):
		length = len(lines)
	lines = ",".join(lines[:length])
	output.write(distinct_word[0] + " " + lines + "]\n\n")
file.close()
output.close()
