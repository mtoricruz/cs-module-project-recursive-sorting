# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # final output array
    merged_arr = []
    # creating variables for the indicies of arrA, arrB
    a_idx = 0
    b_idx = 0

    # while there are elements in both the left & right arrays
    while a_idx<len(arrA) and b_idx<len(arrB):
        # if value of a_index in arrA is smaller than value of b_index in arrB 
        if arrA[a_idx] < arrB[b_idx]:
            # append value of a_index to merged_arr
            merged_arr.append(arrA[a_idx])
            # increment a_index in arrA
            a_idx+=1
        # if value of a_index in arrA is greater than value of b_index in arrB
        else:
            # append value of b_index to merged_arr
            merged_arr.append(arrB[b_idx])
            # incremend b_index in arrB
            b_idx+=1
    # if a_index is the same length of the array 
    if a_idx==len(arrA):
        # assume it is the smallest value left and extend b_index value of arrB
        merged_arr.extend(arrB[b_idx:])
    else:
        # assume it is the highest value left and extend a_index value of arrA
        merged_arr.extend(arrA[a_idx:])
    # return merged arr
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if len of array is <= 1 it is already sorted, so return arr
    if len(arr) <= 1:
        return arr
    
    # finding midpoint of array by dividing length of array by 2
    midpoint = int(len(arr)//2)

    # left half is everything up to the midpoint
    left = merge_sort(arr[:midpoint])
    # right half is everything after the midpoint
    right = merge_sort(arr[midpoint:])

    # after merge_sort is complete, merge these sides
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

