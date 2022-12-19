class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words)\
                or not all(isinstance(coef, float) for coef in coefs)\
                or not all(isinstance(word, str) for word in words):
            return -1
        return sum(k * len(v) for k, v in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words)\
                or not all(isinstance(coef, float) for coef in coefs)\
                or not all(isinstance(word, str) for word in words):
            return -1
        return sum(len(words[k]) * v for k, v in enumerate(coefs))


if __name__ == "__main__":
    coefs = [42., 0.]
    words = ["42", "42", "42"]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (not same len)")
    else:
        print("NOT OK")

    coefs = [42., 0., "21"]
    words = ["42", "42", "42"]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (1 coef is str)")
    else:
        print("NOT OK")

    coefs = [42., 0., 1]
    words = ["42", "42", "42"]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (1 coef is not float)")
    else:
        print("NOT OK")

    coefs = [42., 0., "123"]
    words = ["42", "42", "42"]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (coef is not float)")
    else:
        print("NOT OK")

    coefs = [42., 0., 0.]
    words = ["42", "42", "42"]
    if Evaluator.zip_evaluate(coefs, words) != -1 and Evaluator.enumerate_evaluate(coefs, words) != -1:
        print(f"OK (good) res = 84 ? ({Evaluator.zip_evaluate(coefs, words), Evaluator.enumerate_evaluate(coefs, words)})")
    else:
        print("NOT OK")

    coefs = [42., 0., 0.]
    words = ["42", "42"]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (not same len)")
    else:
        print("NOT OK")

    coefs = [42., 0.]
    words = ["42", 1]
    if Evaluator.zip_evaluate(coefs, words) == -1 and Evaluator.enumerate_evaluate(coefs, words) == -1:
        print("OK (not str word)")
    else:
        print("NOT OK")

    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(f"{Evaluator.zip_evaluate(coefs, words), Evaluator.enumerate_evaluate(coefs, words)} == 32.0 32.0")
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(f"{Evaluator.zip_evaluate(coefs, words), Evaluator.enumerate_evaluate(coefs, words)} == -1 -1")

