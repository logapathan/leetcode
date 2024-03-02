l=int(input("Enter the list size"))
nums=[]

for i in range(l):
    num=int(input("Enter the elements"))
    nums.append(num)


def sortedSquares(nums):
    squares = []
    for num in nums:
        squares.append(num * num)
    squares.sort()
    return squares
print(nums)
square=sortedSquares(nums)
print(square)