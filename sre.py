def reverse(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse("what you think you can do it...that one you really love it."))
print(reverse("Python Exercises."))
