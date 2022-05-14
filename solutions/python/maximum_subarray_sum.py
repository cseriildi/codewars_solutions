# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

def max_sequence(arr):
    subarr = []
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            if i<=j and (sum(subarr) <= sum(arr[i:j])):
                print(i, j)
                subarr = arr[i:j]
    if sum(subarr)<0:
        return 0
    else:
        return sum(subarr)