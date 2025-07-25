def cats_dogs(dictionary, string):
    if string == "":
        return [""] 

    new_list = []

    for i in range(1, len(string) + 1):
        word = string[:i]
        if word in dictionary:
            rest_sentences = cats_dogs(dictionary, string[i:])  
            for sentence in rest_sentences:
                if sentence == "":
                    new_list.append(word)
                else:
                    new_list.append(word + " " + sentence)

    return new_list

string = 'catsanddog'
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(cats_dogs(wordDict, string))
