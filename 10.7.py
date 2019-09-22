#Prog 10.7
lst = list(input('Enter any string: '))
print(lst)
def has_duplicates(lst):
    i = 0
    count = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            count += 1
            i += 2
            return True
        else:
            count = 0
            i += 1
    return False
print(has_duplicates(lst))
