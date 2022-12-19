import random
import sys


def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    options = ["shuffle", "unique", "ordered", None]
    if not isinstance(text, str) or not isinstance(sep, str) or option not in options:
        yield "ERROR"
        return
    res = None
    splitter = text.split(sep)
    if option == "unique":
        res = list(dict.fromkeys(splitter))
    elif option == "ordered":
        splitter.sort()
        res = splitter
    elif option == "shuffle":
        res = []
        while len(splitter) > 0:
            ind = random.randint(0, len(splitter) - 1)
            res.append(splitter[ind])
            del splitter[ind]
    else:
        res = splitter
    for i in res:
        yield i


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    print("Normal")
    for word in generator(text, sep=" "):
        print(word)
    print("\nShuffle")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("\nOrdered")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("\nUnique")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
