#prog 10.5
lst = list(input('Enter anything: '))
print(lst)
def is_sorted(lst):
    if lst != lst.sort():
        lst.sort()
        return True
    return False
print(is_sorted(lst))
print(lst)
