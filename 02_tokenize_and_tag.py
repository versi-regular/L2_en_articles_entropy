import subprocess
import nltk
import string

lang = input("Select language to generate output for (en/sr): ")

# remove punctuation
translateRule = {ord(char): " " for char in string.punctuation.replace("-","")}

fileName = "tokenizer_input_" + str(lang) + ".txt"
outputFileName = "tokenizer_output_" + str(lang) + ".txt"

with open(fileName) as inputFile:
	for line in inputFile:
		if lang == "sr":
			bashCommand = "echo" + " " + line.strip("\n") + " | ./reldi-tokeniser/tokeniser.py sr | ./reldi-tagger/tagger.py sr"
			process = subprocess.getoutput(bashCommand)
		elif lang == "en":
			process = ""
			tokenized_tagged = nltk.pos_tag(nltk.word_tokenize(line.lower().translate(translateRule)))
			i = 0
			process += "0.0.0." + "\t" + "<seg>" + "\t" + "<seg>" + "\n"
			for entity in tokenized_tagged:
				i += 1
				process += "1.1." + str(i) + "." + "\t" + str(entity[0]) + "\t" + str(entity[1]) + "\n"
			process += "0.0.0." + "\t" + "<seg>" + "\t" + "<seg>" + "\n"
		else:
			print("You have a typo or are trying a language this script was not meant for.")
		with open(outputFileName, "a") as outputFile:
			outputFile.write(process.strip(" "))

print("Finished writing data to:", outputFileName)