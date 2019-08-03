from nltk import word_tokenize, sent_tokenize
from nltk.util import ngrams

bigrams = ""

lang = input("Select language to generate output for (en/sr): ")

fileName = "tokenizer_input_" + str(lang) + ".txt"
outputFileName = "ngram_output_" + str(lang) + ".txt"

with open(fileName) as inputFile:
	text = inputFile.read()
	text = text.replace('\n',' ')

tokenized = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(text)]

for sentence in tokenized:
	bigrams = ngrams(sentence, 2)
	bigrams_in_sentence =  [' '.join(word) for word in bigrams]
	for bigram in bigrams_in_sentence:
		with open(outputFileName, "a") as outputFile:
			outputFile.write(bigram)
			outputFile.write("\n")
