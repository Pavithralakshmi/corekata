def reverseWordSentence(Sentence):
	return ' '.join(word[::-1] for word in Sentence.split(" "))
Sentence = "uyutyutuyutyututyutyu"
print(reverseWordSentence(Sentence)) 
