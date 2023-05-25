
def buble_sort(some_list):
    flag = False
    while flag == False:

        count = 0
        for i in some_list:
            if count < len(some_list)-1:
                if i > some_list[count+1]:
                    some_list[count], some_list[count+1] = some_list[count+1], some_list[count]
                count += 1
        if some_list == sorted(some_list):
            flag = True

    return some_list

my_list = buble_sort([7,1,3,8,9,4,5,2,10,11])
print(my_list)

def binary_search(some_list,value):
    val = value
    result = False
    first = 0
    last = len(my_list)-1

    while result == False:
        if first <= last:
            middle = (first+last)//2
            if val == my_list[middle]:
                first = middle
                last = first
                result = True
                pos = middle
            else:
                if val > my_list[middle]:
                    first = middle+1
                else:
                    last = middle-1

        else:
                return "элемент не найден"

    else:
        return "Элемент найден под индексом: " + str(my_list[pos])


print(binary_search(my_list,11))




