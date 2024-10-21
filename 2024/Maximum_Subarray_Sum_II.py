# Maximum Subarray Sum II
# https://www.codewars.com/kata/56e3cbb5a28956899400073f
# Difficulty: 5 kyu

def find_subarr_maxsum(arr):
    max_arr, curr = [], []
    max_sum, curr_sum = 0, 0
    
    for index, num in enumerate(arr):
        if curr_sum == 0:
            curr.append(index)
        if curr_sum + num < 0:
            curr.clear()
        curr_sum = max(0, curr_sum + num)
            
        if curr_sum >= max_sum:
            if curr_sum > max_sum:
                 max_arr.clear()
            max_sum = curr_sum
            for start in curr:
                max_arr.append(arr[start : index + 1])
    
    if len(max_arr) == 1:
        max_arr = max_arr[0]
    return [max_arr, max_sum]