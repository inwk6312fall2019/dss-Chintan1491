#Program 10.3
l = [1,2,3,4,5,6,7]
def middle(l):
    new_list = []
    for num in l[1:6]:
        new_list.append(num)
    return new_list
print(l)
print(middle(l))
