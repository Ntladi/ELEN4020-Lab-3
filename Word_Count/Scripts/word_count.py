import mrs
import string
import re
import stop_words

wordRe = re.compile(r"[\w']+")
stopWords = stop_words.get_stop_words()

class Word_Count(mrs.MapReduce):
	def map(self,lineNumber,text):
		for word in wordRe.findall(text):
			if not word.isdigit() and word.lower() not in stopWords:
				word = word.strip(string.punctuation)
				yield(word.lower(),1)

	def reduce(self,word,count):
		yield sum(count)

if __name__ == '__main__':
	mrs.main(Word_Count)
