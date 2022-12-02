import sys

MORSE_CODE_DEF = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	" ": "/"
}

if __name__ == '__main__':
	text = str()
	if len(sys.argv) == 1:
		sys.exit("No args provided")
	elif len(sys.argv) > 2:
		for i in range(1, len(sys.argv)):
			text += (sys.argv[i] + " ")
		text = text[:len(text) - 1]
	else:
		text = sys.argv[1]
	res = str()
	for c in text:
		try:
			morse_code = MORSE_CODE_DEF[c.upper()]
		except KeyError:
			sys.exit("ERROR")
		if not morse_code:
			sys.exit("ERROR")
		res += morse_code + " "
	print(res[:len(res) - 1])
