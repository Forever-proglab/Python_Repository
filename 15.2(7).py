nums = []
n_of_nums = int(input())
elem = 0
max = 0
for i in range(n_of_nums):
    elem = int(input())
    if elem > max and elem % 4 == 0:
        max = elem
    nums.append(elem)
print(nums)
print(max)