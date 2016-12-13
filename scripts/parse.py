import re

number = {'1': 's a t u', '2': 'd u a', '3': 't i g a', \
		  '4': 'e m p a t', '5': 'l i m a', '6': 'e n a m', \
		  '7': 't u j u h', '8': 'd e l a p a n', '9': 's e m b i l a n', \
		  '0': 'n o l'}

phonem = {'a': 'a', 'au': 'aw', 'ai': 'ay', 'b': 'b', \
		  'c': 'c', 'd': 'd', 'e': 'e', 'E': 'ee', \
		  'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', \
		  'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', \
		  'n': 'n', 'ny': 'ny', 'ng': 'ng', 'o': 'o', \
		  'oi': 'oy', 'p': 'p', 'r': 'r', 's': 's', \
		  'sy': 'sy', 't': 't', 'u': 'u', 'v': 'f', \
		  'w': 'w', 'kh': 'kh', 'y': 'y', 'z': 'z', \
		  'xb': 's', 'xe': 'ks', 'q': 'q' }

ignore = ['\n']

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

def is_next(chars, idx, char):
	if (idx > len(chars) - 1):
		return False
	else:
		return (chars[idx] == char)

def monophoning(text):
	monophones = []
	text = re.sub('[^0-9a-zA-Z]+', '', text)
	
	chars = list(text)
	charn = 0

	while (charn < len(text)):
		char = chars[charn]
		if (char != 'e' and char != 'E'):
			char = char.lower()

		if (char in ignore):
			None			
		elif (is_number(char)):
			monophones.append(number[char])
		elif (char == 'x'):
			if (charn == 0):
				monophones.append(phonem['xb'])
			else:
				monophones.append(phonem['xe'])
		elif (char == 'a'):
			if (is_next(chars, charn, 'u')):
				monophones.append(phonem['au'])
				charn += 1
			elif (is_next(chars, charn, 'i')):
				monophones.append(phonem['ai'])
				charn += 1
			else:
				monophones.append(phonem['a'])
		elif (char == 'n'):
			if (is_next(chars, charn, 'y')):
				monophones.append(phonem['ny'])
				charn += 1
			elif (is_next(chars, charn, 'g')):
				monophones.append(phonem['ng'])
				charn += 1
			else:
				monophones.append(phonem['n'])
		elif (char == 'o'):
			if (is_next(chars, charn, 'i')):
				monophones.append(phonem['oi'])
				charn += 1
			else:
				monophones.append(phonem['o'])
		elif (char == 's'):
			if (is_next(chars, charn, 'y')):
				monophones.append(phonem['sy'])
				charn += 1
			else:
				monophones.append(phonem['s'])
		elif (char == 'k'):
			if (is_next(chars, charn, 'h')):
				monophones.append(phonem['kh'])
				charn += 1
			else:
				monophones.append(phonem['k'])
		else:
			monophones.append(phonem[char])
		charn += 1

	return monophones


infile = open('lexicon.txt', 'r')
oufile = open('olist.txt', 'w')

for line in infile:
	words = line.split()
	if (line != '\n'):
		oufile.write(words[0].lower() + "\t[" + words[0].lower() + "]\t" + " ".join(words[1:]) + '\n')

oufile.close()