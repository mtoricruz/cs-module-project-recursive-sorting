 # TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    while start <= end:
        midpoint = start + (end - start) // 2
        mid_value = arr[midpoint]

        if mid_value == target:
            return midpoint
        elif target < mid_value:
            return binary_search(arr, target, start, midpoint - 1)
        else:
            return binary_search(arr, target, midpoint + 1, end)
    return - 1

# Question: I edited my iterative version to pass the recursive test. On my iterative version, i explicitly state the start/end point and store them in start/end index variables, why does that break here in a recursive search? Isn't the start/end index a base case itself?

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
