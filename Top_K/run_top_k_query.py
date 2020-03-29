import sys
import shutil, os
import time

def sort_words(countPairs):
	# This method sorts the list of words in decending order and returns the result
	# as a key value pair
	allCountPairs = sorted(countPairs, key = lambda wordPair: wordPair[1], reverse = True)
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
fileName = sys.argv[1]
output = "Output"
countPairs = []	
print("Running MapReduce using Mrs-MapReduce for top-k query on " + fileName + "\n")
startTime = time.time()	
os.system("python3 word_count.py " + fileName + " Output")
file = open("Output/source_0_split_0_.mtxt", "r")
output = open("Output/top_k_output.txt","w")
words = file.readlines()

for wordInfo in words:
	key,frequency = wordInfo.split()
	countPairs.append([key, frequency])

allCountPairs = sort_words(countPairs)
endTime = time.time()
totalTime = (endTime - startTime)
output.write("The proccess took " + str(totalTime) + " seconds\n")
get_top_k_words(allCountPairs,10,output)
get_top_k_words(allCountPairs,20,output)
file.close()
output.close()
os.system("rm Output/source_0_split_0_.mtxt")
print("Top K complete")
