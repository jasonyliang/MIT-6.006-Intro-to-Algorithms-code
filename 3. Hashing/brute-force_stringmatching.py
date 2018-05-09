def bruteforce(word, text):
    m = len(word)
    n = len(text)

    for i in range(0,n-m-1):
        if text[i:i+m] == word:
            return "Text match starting at", i
    
    return "Text not found"
string = 'hahahahahhahellohahaha'
word = "hello"

print(bruteforce(word, string))