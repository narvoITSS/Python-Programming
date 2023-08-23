def reverse3(nums):
    reverse_nums = []
    reverse_index = -1
    for index in range(len(nums)):
        reverse_nums.append(nums[reverse_index])
        reverse_index -= 1
    return(reverse_nums)

def main():
    print(reverse3([5,11,9]))

if __name__ == "__main__":
    main()