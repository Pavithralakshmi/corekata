def rev(word):
    a = word.split(" ")
    a=a[-1::-1]
    output = ' '.join(a)
     
    return output
 
if __name__ == "__main__":
    word = raw_input("enter string: ");
    print rev(word)
