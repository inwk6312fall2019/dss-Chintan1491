#prog 10.2
lst = [1,2,3,4,5,6,7,8,9]
def cumsum(lst):
    lstsum = []
    total_sum = 0
    for num in lst:
        total_sum += num
        lstsum.append(total_sum)
    return lstsum
print(cumsum(lst))
