vowels=['a','e','i','o','u']
a=raw_input("enter your letter")
if a in vowels:
    print("its vowel",a)
elif a>0:
    print("please enter valid letters")
else:
    print("its constant",a)
