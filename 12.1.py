#prog 12.1

def most_frequent(sample):
    d = dict()
    for s in sample:
        if s.isupper():
            s = s.lower()
            d[s] = 1 + d.get(s, 0)
        else:
            s = s.lower()
            d[s] = 1 + d.get(s, 0)
    t = []
    for (y,z) in reversed(sorted(zip(d.values(), d.keys()))):
        t.append([z, y/len(sample) * 100])
    return t
sample = open('samplestory.txt')
for line in sample:
    word = line.strip()
print(most_frequent(word))
