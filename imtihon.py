# my_list = []
# for i in range(1,21):
#     my_list.append(i)
# print(my_list)
my_list = [10, 2, 3, 14, 5, 16, 7, 8, 19, 1,12, 13, 4, 15, 6, 17, 18, 9, 20]

def quick_sort(top):
    a=len(top)
    if a<2:
        return top
    else:
        right_list = []
        left_list = []
        pivot = top.pop()
        for i in top:
            if pivot<i:
                right_list.append(i)
            else:
                left_list.append(i)
    return quick_sort(left_list)+[pivot]+quick_sort(right_list)
print(quick_sort(my_list))

a=quick_sort(my_list)



def func(my_lis):
    for i in range(1, (my_lis[-1]+1)):
        if i!=a[i-1]:
            return i
print(func(a))




