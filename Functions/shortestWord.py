def shortestWord(str):
    #Given a string of words, return the length of the shortest word(s).
    result = 0;
    for word in str.split():
        if result == 0 or result > len(word):
            result = len(word)
    return result
print(shortestWord("The quick brown fox jumped over the lazy dog"))
print(shortestWord("bitcoin take over the world maybe who knows perhaps"))
print(shortestWord("turns out random test cases are easier than writing out basic ones"))
print(shortestWord("lets talk about javascript the best language"))
print(shortestWord("let's travel abroad shall we"))