def find_duplicate(nums):
    # Finding the intersection point
    tortoise = nums[0]
    hare = nums[0]

    # Move tortoise by 1 and hare by 2 until they meet
    while True:
        tortoise = nums[tortoise]  # move tortoise one step
        hare = nums[nums[hare]]    # move hare two steps
        if tortoise == hare:
            break

    # Finding the entrance to the cycle
    tortoise = nums[0]  # reset tortoise to the beginning

    while tortoise != hare:
        tortoise = nums[tortoise]  # move tortoise one step
        hare = nums[hare]          # move hare one step

    return hare  # or return tortoise; both are at the duplicate

# Example usage:
input_array = [1, 3, 4, 2, 2]
output = find_duplicate(input_array)
print(output)
