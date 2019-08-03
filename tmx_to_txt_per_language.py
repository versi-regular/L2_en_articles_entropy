from translate.storage.tmx import tmxfile

with open("en-sr.tmx", 'rb') as inputFile:
	processedFile = tmxfile(inputFile, 'en', 'sr')
	for entry in processedFile.unit_iter():
		# English
		print(entry.getsource())
		# Serbian
		print(entry.gettarget())