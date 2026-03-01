import random

# Step 1 — Generate Data
# Generate 30 random integers between 1 and 100
def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

# Step 2 - Compute minimum
def compute_minimum(nums):
    if not nums:
        return None
    
    min_value = nums[0]
    for num in nums[1:]:
        if num < min_value:
            min_value = num
    return min_value

# Step 3 - Compute maximum
def compute_maximum(nums):
    if not nums:
        return None
    
    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num
    return max_value


# Step 3 - Compute mean
def compute_mean(nums):
    if not nums:
        return None
    
    total_sum = 0
    for num in nums:
        total_sum += num
    count = len(nums)
    mean_value = total_sum / count
    return mean_value

# Step 4 - Numbers above mean

def numbers_above_mean(nums):
    if not nums:
        return []
    
    mean_value = compute_mean(nums)
    numbers_above_list = [num for num in nums if num > mean_value]
    return numbers_above_list

def compute(nums):
    if not nums:
        return None
    min_value = nums[0]
    max_value = nums[0]
    total_sum = nums[0]
    for num in nums[1:]:
        total_sum += num
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    mean_value = total_sum / len(nums)

    return min_value, max_value, mean_value



if __name__ == "__main__":
    # Generate random numbers
    numbers = generate_random_numbers(30, 1, 100)
    print("Generated numbers:", numbers)

    minimum_value = compute_minimum(numbers)  
    print("Minimum value:", minimum_value)

    maximum_value = compute_maximum(numbers)
    print("Maximum value:", maximum_value)
    
    mean_value = compute_mean(numbers)
    print("Mean value:", mean_value)

    above_mean_numbers = numbers_above_mean(numbers)
    print("Numbers above mean:", above_mean_numbers)
    min_value, max_value, mean_value = compute(numbers)
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
    print("Mean value:", mean_value)