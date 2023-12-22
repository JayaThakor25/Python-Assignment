#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Hello Python . It Is good Language . It IS very easy'))
