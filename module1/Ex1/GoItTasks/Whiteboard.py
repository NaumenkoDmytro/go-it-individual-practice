def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        print(f'is left index = {left}')
        print(f'is right index = {right}')
        curr_sum = numbers[left] + numbers[right] # here we add two numbers based on their idexes
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1 #we move index here
        else:
            right -= 1 # we move index here

print(twoSum([1,2,3,4,5,6,7], 100))

# numbers = [1,2]
# curr_sum = numbers[0] + numbers[1]
# print(curr_sum)


# to get the full control of index we need assing this to variable and work with it in case of math operations