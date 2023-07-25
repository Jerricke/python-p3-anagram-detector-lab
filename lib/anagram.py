# your code goes here!


class Anagram:
    def __init__(self, target):
        self.target = target

    def match(self, words):
        result = []
        for word in words:
            if set(word) == set(self.target):
                result.append(word)
            else:
                return result
        return result

    pass
