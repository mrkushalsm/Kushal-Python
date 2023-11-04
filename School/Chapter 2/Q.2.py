sentence = input("Enter a sentence: ")
print("\"" + sentence + "\"")
alphanum, word, characters = 0, 0, 0
for i in sentence:
    if i.isalnum():
        alphanum +=1
    if i.isspace() or characters == len(sentence) - 1:
        word += 1
    characters += 1
print("No. of words=", word)
print("No. of characters=", characters)
print("Percentage of characters that are alpha numeric=", str((alphanum/characters)*100) + "%")
