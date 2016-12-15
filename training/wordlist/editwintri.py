phones = []
with open("fulllist") as f:
	phones = f.readlines()
output = open("wintrinew.mlf","w")
with open("wintri.mlf") as f:
	for line in f:
		if (line.startswith('"') or line.startswith('#') or line.startswith('.') or line in phones):
			output.write(line)
