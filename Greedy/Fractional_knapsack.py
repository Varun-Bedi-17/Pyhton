# We can take fractional values also
# Leetcode-1710

def fract_knap(arr, W):
    arr.sort(key = lambda x: x[0]/x[1], reverse = True)

    answer = 0.0

    for i in range(len(arr)):
        if W >= arr[i][1]:
            answer += arr[i][0] 
            W -= arr[i][1]

        else:
            answer += (arr[i][0]/arr[i][1]) *W
            break

    return answer

Weight_Value = [[60,10], [100,20], [120,30]]       #   (value,weight)
print(fract_knap(Weight_Value, 50))




#  When weight and value stored as class     ( GFG Solution )

# def fract_knap_class(Items, W):                            # Items is class of value and weight.
#     Items.sort(key = lambda x: x.value/x.weight, reverse = True)

#     answer = 0.0
    
#     for item in Items:
#         if W >= item.weight:
#             answer += item.value 
#             W -= item.weight
    
#         else:
#             answer += (item.value/item.weight) *W
#             break
    
#     return answer