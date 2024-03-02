l = int(input("Enter the list size"))
nums = []

for i in range(l):
    num = int(input("Enter the elements"))
    nums.append(num)


def majorityElement(nums):
    l = len(nums)
    a = []
    for i in range(0, l):
        freq = 1
        for b in range(i):
            if nums[i] == nums[b]:
                break

        for j in range(1, l - i):
            if nums[i] == nums[i + j]:
                freq += 1
        if freq > l / 3:
            a.append(nums[i])

    return a


set = majorityElement(nums)
print(set)