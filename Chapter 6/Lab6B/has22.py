'''Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''
# https://codingbat.com/prob/p119308
def has22(nums):
    for index in range(len(nums)):
        if nums[index] == 2:
            if index == 0:
                if nums[index+1] == 2:
                    return(True)
            elif index == (len(nums)-1):
                if nums[index-1] == 2:
                    return(True)
            elif nums[index-1] == 2 or nums[index+1] == 2:
                return(True)
            else:
                return(False)
        else:
            pass

def main():
    print(has22([1,2,1,2,22,3,4,5,2,2]))

if __name__ == "__main__": main()