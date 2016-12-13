import re

def sanitize(infile, oufile, scpfile, ousfile):
	oufile.write("#!MLF!#\n")
	filename = "unknown.lab"

	scp = {}
	linenum = 0
	words = []
	begin = False

	for line in scpfile:
		temp = line[-18:]
		temp = temp[:-5]
		scp[temp] = line[:-18]

	for line in infile:
		if (line[0] == "\""):
			begin = True
			filename = re.sub('[\"\n]','',line)
		elif (begin):
			if (line[0] == "."):
				begin = False
				if (len(words) != 0):
					print(filename + " | " + str(len(words)) + " > " + scp[filename[2:-4]])
					oufile.write("\"" + filename + "\"\n")
					for word in words:
						oufile.write(word)
					oufile.write(".\n")
					ousfile.write(scp[filename[2:-4]] + filename[2:-4] + ".mfc\n")
				words = []
				linenum += 1
			else:
				words.append(line)
		
scpfile = open('train.scp', 'r')
wordfile = open('words.mlf', 'r')
oufile = open('words_sanitize.mlf', 'w')
ousfile = open('train_sanitize.scp', 'w')

sanitize(wordfile, oufile, scpfile, ousfile)

oufile.close()
ousfile.close()
