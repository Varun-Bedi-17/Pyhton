# Shell sort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead.
#  When an element has to be moved far ahead, many movements are involved. 

def shell_sort(arr):
    n = len(arr)
    gap=n//2
       
    while gap>0:
        j=gap

        while j<n:
            i=j-gap
              
            while i>=0:

                if arr[i+gap]>arr[i]:          # We can't use j here because we have to swap elements according to i
                    break               
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
  
                i=i-gap
            j+=1
        gap=gap//2

  

arr2 = [12, 34, 54, 2, 3]
  
shell_sort(arr2)
print(arr2)

arr = [170, 45, 75, 90, 802, 24, 2, 66]
shell_sort(arr)
print(arr)
    
data = [4, 2, 2, 8, 3, 3, 1]
shell_sort(data)
print(data)

array = [64, 25, 12, 22, 11]
shell_sort(array)
print(array)

array2 = [12, 11, 13, 5, 6, 7]
shell_sort(array2)
print(array2)




##  Another method
# def shellSort(arr):
#     n = len(arr)
#     gap=n//2
       
#     while gap>0:
#         j=gap

#         while j<n:                 #######  Read after this
#             i=j-gap
#             k = j
              
#             while i>=0:

#                 if arr[k] > arr[i]:          
#                     break               
#                 else:
#                     arr[i],arr[k]=arr[k],arr[i]
#                     k = k-gap
  
#                 i=i-gap
#             j+=1

# data = [12, 34, 54, 2, 3]
  
# shell_sort(data)
# print(data)

# data1 = [170, 45, 75, 90, 802, 24, 2, 66]
# shell_sort(data1)
# print(data1)
    
# data2 = [4, 2, 2, 8, 3, 3, 1]
# shell_sort(data2)
# print(data2)

# data3 = [64, 25, 12, 22, 11]
# shell_sort(data3)
# print(data3)

# data4 = [12, 11, 13, 5, 6, 7]
# shell_sort(data4)
# print(data4)
