import mrs
import string
import re
import stop_words

wordRe = re.compile(r"[\w']+")
stopWords = stop_words.get_stop_words()

class Inverted_Index(mrs.MapReduce):
	def map(self,lineNumber,text):
		for word in wordRe.findall(text):
			if not word.isdigit() and word.lower() not in stopWords:
				word = word.strip(string.punctuation)
				yield(word.lower(),lineNumber)

	def reduce(self,word,count):
		yield word,list(count)

if __name__ == '__main__':
	mrs.main(Inverted_Index)