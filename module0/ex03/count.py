import string
import sys


def text_analyzer(text=""):
    """
    Takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, punctuation characters and
    spaces.
    :param text: text
    :return: None
    """
    if text is None or not text:
        print("What is the text to analyze?")
        try:
            res = input()
            text_analyzer(res)
        except EOFError or KeyboardInterrupt:
            return
        return
    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0

    for char in text:
        if char in string.ascii_lowercase:
            lower += 1
        elif char in string.ascii_uppercase:
            upper += 1
        elif char == ' ':
            spaces += 1
        elif char in string.punctuation:
            punctuation += 1

    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Only one arg must be provided")
    text_analyzer(sys.argv[1])
