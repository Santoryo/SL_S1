file = open('dorian.txt')

locc = {}

for line in file:
    line = line.strip().lower()
    for letter in line:
        if letter not in locc:
            locc[letter] = 1
        else:
            locc[letter] += 1


rlocc = {}

for letter, index in locc.items():
    if index not in rlocc:
        rlocc[index] = [letter]
    else:
        rlocc[index].append(letter)

i = 0

# Letters statistic most/least common
print("Letter statistics:")
print("- 5 most common letters/chars")
for n, l in reversed(sorted(rlocc.items())):
    if i < 5:
        print(f"letter/char '{l}' found {n} times")
        i += 1

print("- 5 most common letters/chars")
i = 0
for n, l in reversed(sorted(rlocc.items(), reverse=True)):
    if i < 5:
        print(f"letters/chars '{l}' found {n} times")
        i += 1

wocc, wlen = {}, {}

for line in file:
    words = line.strip().lower().split()
    print(words)
    for w in words:
        w = w.strip(".,;:-'`\"?!()")
        if not (w in wocc):
            wocc[w] = 1
            wlen[w] = len(w)
        else:
            wocc[w] += 1

file = open('dorian.txt')

wocc, wlen = {}, {}

for line in file:
    words = line.strip().lower().split()
    for w in words:
        w = w.strip(".,;:-'`\"?!()")
        if not (w in wocc):
            wocc[w] = 1
            wlen[w] = len(w)
        else:
            wocc[w] += 1

sortedwocc = sorted(wocc, key=wocc.get, reverse=True)
wlen = sorted(wlen, key=wlen.get, reverse=True)
lastLength = 0
print(f"Words statistics:")
print(f" - number of unique words: {len(wocc)}")
print(f" - 5 most common words: ")
for word in sortedwocc:
    if i < 5:
        print(f"word '{word}' found {wocc[word]} times,")
        i += 1
    else:
        break
print(f"- the longest words (with 5 longest lengths):")
i = 0
text = ""
for word in (wlen):
    if i < 5 or lastLength == len(word):
        if lastLength != len(word):
            text += f"\nwords of length '{len(word)}' are {word},"
            i += 1
        else:
            text += f" {word}"
            i - 1
        lastLength = len(word)
    else:
        break
print(text)
file.close()
