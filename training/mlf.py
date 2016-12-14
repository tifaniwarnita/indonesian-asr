import re

def make_mlf(infile, oufile, front):
	for line in infile:
		data = line.split("\t")
		words = data[1].split()

		clas = data[0].split("_")
		oufile.write("\"*/" + front + clas[1] + ".lab\"\n")

		for word in words:
			word = re.sub('[^0-9a-zA-Z-]+', '', word)
			oufile.write(word.lower() + "\n")

		oufile.write(".\n")
		
frontA = "A11LTL004A"
frontB = "A12LJM016B"
frontC = "B11LPM087C"
frontD = "A24LAM052D"
frontE = "B11LJM070E"
frontF = "B12LTM128F"
frontG = "B12LPM188G"
frontH = "A24LMM075H"
frontI = "B11LMM194I"
frontJ = "B11LTL182J"

afile = open('dataset/train/transcript/A-raw.tsv', 'r')
bfile = open('dataset/train/transcript/B-raw.tsv', 'r')
cfile = open('dataset/train/transcript/C-raw.tsv', 'r')
dfile = open('dataset/train/transcript/D-raw.tsv', 'r')
efile = open('dataset/train/transcript/E-raw.tsv', 'r')
ffile = open('dataset/train/transcript/F-raw.tsv', 'r')
gfile = open('dataset/train/transcript/G-raw.tsv', 'r')
hfile = open('dataset/train/transcript/H-raw.tsv', 'r')
ifile = open('dataset/train/transcript/I-raw.tsv', 'r')
jfile = open('dataset/train/transcript/J-raw.tsv', 'r')

oufile = open('wordlist/words.mlf', 'w')
oufile.write("#!MLF!#\n")

make_mlf(afile, oufile, frontA)
make_mlf(bfile, oufile, frontB)
make_mlf(cfile, oufile, frontC)
make_mlf(dfile, oufile, frontD)
make_mlf(efile, oufile, frontE)
make_mlf(ffile, oufile, frontF)
make_mlf(gfile, oufile, frontG)
make_mlf(hfile, oufile, frontH)
make_mlf(ifile, oufile, frontI)
make_mlf(jfile, oufile, frontJ)

oufile.close()
