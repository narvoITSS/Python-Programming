'''Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.'''
# https://codingbat.com/prob/p184853

def big_diff(nums):
    maxValue = nums[0]
    minValue = nums[0]
    for index in range(len(nums)):
        if nums[index] >= maxValue: maxValue = nums[index]
        else: pass
        if nums[index] <= minValue: minValue = nums[index]
        else: pass
    return(maxValue-minValue)
        
def main():
    print(big_diff([2,10,7,2]))

if __name__ == "__main__":
    main()