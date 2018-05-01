def separate_string(sentence):
    l = list(sentence)
    list_even = list()
    list_odd = list()
    index = 0

    for letter in l:
        if index % 2 != 0:
            list_even.append(letter)
            
        else:
            list_odd.append(letter)
            
        index += 1

    string_even = "".join(list_even)
    string_odd = " ".join(list_odd)
    print(sentence[::-1])

sentence=str(input("enter:"))
separate_string(sentence)
