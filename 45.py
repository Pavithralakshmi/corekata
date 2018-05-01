sentence = str(input("enter"))

sentence_count = 1
new_sentence = []
for word in sentence.split():
    if not sentence_count % 2 == 0:
        new_sentence.append(word.title() + " ")
    else:
        new_sentence.append(word + " ")
    sentence_count += 1

print "".join(new_sentence)
