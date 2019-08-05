posFileName = "tokenizer_output_" + "en" + ".txt"
outputFileName = "filtered_tagged_ngrams_" + "en" + ".txt"

with open(outputFileName, "a") as outputFile:
	with open(posFileName) as posFile:
		taggedTokens = posFile.readlines()
		for i in range(len(taggedTokens)):
			trash, word, tag = taggedTokens[i].strip().split("\t")
			if tag.startswith("NN"):
				# previous word to build bi-gram
				ptrash, pword, ptag = taggedTokens[i-1].strip().split("\t")
				outputFile.write(pword + " " + word + "\t" + ptag + " " + tag + "\n")