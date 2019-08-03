from translate.storage.tmx import tmxfile

temp = ""
lang = input("Select language to generate output for (en/sr): ")

with open("en-sr.tmx", 'rb') as inputFile:
	processedFile = tmxfile(inputFile, 'en', 'sr')
	for entry in processedFile.unit_iter():
		if lang == "en":
			temp += entry.getsource() + "\n"
		elif lang == "sr":
			temp += entry.gettarget() + "\n"
		else:
			print("You have a typo or are trying a language this script was not meant for.")

fileName = "tokenizer_input_" + str(lang) + ".txt"
print("Created file:", fileName)

with open(fileName, "w+") as outputFile:
	outputFile.write(temp)