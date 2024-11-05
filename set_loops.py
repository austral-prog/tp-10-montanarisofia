def unique_strings(words):
    unique=set()
    for word in words:
        if word not in unique:
            unique.add(word)
    return unique
print(unique_strings("hello"))
