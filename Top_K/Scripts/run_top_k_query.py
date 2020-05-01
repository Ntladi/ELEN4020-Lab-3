import sys
import shutil, os
import time


def compare_by_occurence(countPairs):
	# This function sorts a list in decending order
	return countPairs[1]

def sort_words(countPairs):
	# This method sorts the list of words in decending order and returns the result
	# as a key value pair
	allCountPairs = sorted(countPairs, key = compare_by_occurence, reverse = True)
	return allCountPairs

def get_top_k_words(allCountPairs, k,file):
	# This method outputs the top k words in the output file
	file.write("----- K = {} ------".format(k) + "\n")
	if len(allCountPairs) < k:
		k = len(allCountPairs)
		
	topKWords = allCountPairs[:k]
	for wordPair in topKWords:
		file.write(str(wordPair) + "\n")

# The process is executed below
inputFile = sys.argv[1]
outputFile = sys.argv[2]
queries = sys.argv[3]

if (os.path.isdir("./Temp/")):
    os.system("rm -rf ./Temp/")

countPairs = []
startTime = time.time()	
os.system("python3 ./Scripts/word_count.py " + inputFile + " ./Temp")
file = open("Temp/source_0_split_0_.mtxt", "r")
output = open(outputFile,"w")
words = file.readlines()

for wordInfo in words:
	key,frequency = wordInfo.split(" ")
	countPairs.append([key, int(frequency)])

allCountPairs = sort_words(countPairs)
endTime = time.time()
totalTime = (endTime - startTime)
output.write("The proccess took " + str(totalTime) + " seconds\n")
get_top_k_words(allCountPairs,int(queries),output)

file.close()
output.close()
