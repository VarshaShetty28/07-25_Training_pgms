def group_words(words):
    grouped = {}
    for word in words:
        key = (len(word), word[0])
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(word)
    return grouped


words = ["apple", "bat", "ball", "art", "axe", "cat", "dog", "act", "banana"]
result = group_words(words)
print(result)
