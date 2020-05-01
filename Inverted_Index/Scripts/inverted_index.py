import mrs
import string
import re
import stop_words

wordRe = re.compile(r"[\w']+")
stopWords = stop_words.get_stop_words()

def hasNumbers(word):
	return bool(re.search(r'\d', word))

class Inverted_Index(mrs.MapReduce):
	def map(self,lineNumber,text):
		for word in wordRe.findall(text):
			word = word.translate(str.maketrans("","",string.punctuation))
			word = word.lower()
			if not hasNumbers(word) and word not in stopWords and word != "":
				yield(word,lineNumber)

	def reduce(self,word,count):
		yield word,list(count)

if __name__ == '__main__':
	mrs.main(Inverted_Index)
