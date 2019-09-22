#prog 10.6
def is_anagram(a,b):
    for i in a:
        if i in b:
            return True
        else:
            return False

a = input('Enter 1st string: ')
b = input('Enter 2nd string: ')
print(is_anagram(a,b))
