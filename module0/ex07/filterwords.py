import string
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("ERROR")
    text = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    try:
        length = int(sys.argv[2])
    except ValueError:
        sys.exit("ERROR")
    word_list = text.split(" ")
    print([x for x in word_list if len(x) > length])
