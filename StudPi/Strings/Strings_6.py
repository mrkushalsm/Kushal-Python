sentence = input("Enter a sentence")
length = 0
word = ""
long_word = ""
count = 0
for i in range(0, len(sentence)):
    if sentence[i] == " ":
        if count > length:
            length = count
            long_word = word
        word = ""
        count = 0
    elif i == len(sentence) - 1:
        count += 1
        word += sentence[i]
        i -= 1
        continue
    else:
        word += sentence[i]
        count += 1

print("Longest word is", long_word)
