#Prog 10.4
lst = [1,2,3,4,5,6]
print(lst)
def chop(lst):
    lst.pop(5)
    lst.pop(0)
print(chop(lst))
print(lst)
