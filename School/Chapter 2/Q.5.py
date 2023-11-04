words_list = eval(input("Enter a list of words: "))
for word in words_list:
    index, word_count, count = 0, 0, 0
    for char in word:
        count += 1
    if count > word_count:
        word_count = char
        index = words_list.index(word)
print("The largest word in the words list is \"" + words_list[index] + "\"")
