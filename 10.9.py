#prog 10.9
def version1(fin):
    lst1 = []
    for word in fin:
        char = word.strip()
        lst1.append(char)
    return lst1

def version2(fin):
    lst2 = []
    for word in fin:
        letter = word.strip()
        lst2 = lst2 + [letter]
    return lst2
fin = open('words.txt')
print(version1(fin))
print(version2(fin))

