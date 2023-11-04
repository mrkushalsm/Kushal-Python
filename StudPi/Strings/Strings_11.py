sentence = input("Enter a sentence: ")
word_count = 0
for i in sentence:
    if i.isspace() or i == "," or i == "." or i == ", " or i == ". " or i == sentence[len(sentence) - 1]:
        word_count += 1

# word_count += 1
print("No. of words present in the sentence is", word_count)
