commandline = [1, 200, 3, 4, 500, 6, 7, 8, 9]
print(commandline)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)


# kisi bhi line ka  list ka last vaiable ma value input dena
# used only append
# commandline.append(90)
# commandline.sort()
# commandline.reverse()
# commandline.index(200)
print(commandline.index(200))

#  you can change the value in python using the = it gone a refernce 
print(quick_sort(commandline))