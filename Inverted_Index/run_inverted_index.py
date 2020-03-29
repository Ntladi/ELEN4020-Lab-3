import sys
import shutil, os
import time

filename = sys.argv[1]

def get_key_and_line_numbers(wordData):
	firstBracket = wordData.find("(")
	lastBracket = wordData.find(")")
	wordData = wordData[firstBracket + 1:lastBracket]
	word,lineNumbers = wordData.split(",",1)
	return word,lineNumbers
	
wordsWithLineNumbers = []
print("Running MapReduce using Mrs-MapReduce for Inverted Index on ", filename)
startTime = time.time()	
os.system("python3 inverted_index.py "  + filename + " Output/")
file = open("Output/source_0_split_0_.mtxt", "r")
output = open("Output/inverted_index_output.txt","w")
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
os.system("rm Output/source_0_split_0_.mtxt")
print("Inverted index complete.")