# Re 2. Problems on Recursion | Strivers A2Z DSA Course
def f(x, n):
    if n > 10:
        return 1
    print(x * n)
    f(x, n + 1)


def print_number_reverse(i, n):
    if i > n:
        return
    print_number_reverse(i + 1, n)
    print(i)


def print_number_reverse_v2(n):
    if n > 10:
        return
    print_number_reverse_v2(n + 1)
    print(n)


def print_name(n):
    if n == 0:
        return
    print("Mani Bhushan")
    print_name(n - 1)


# Re 3. Parameterised and Functional Recursion | Strivers A2Z DSA Course

def print_sum_of_numbers(i, sum):
    if i < 1:
        print(sum)
        return
    print_sum_of_numbers(i - 1, sum + i)


def sum_of_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_numbers(n - 1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Re 4. Problems on Functional Recursion | Strivers A2Z DSA Course

def reverse_array_using_recursion(arr, i, j):
    if i > j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    reverse_array_using_recursion(arr, i + 1, j - 1)


def check_palindrome_using_recursion(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return check_palindrome_using_recursion(s, i + 1, j - 1)


def fibonacci_using_recursion(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_using_recursion(n - 1) + fibonacci_using_recursion(n - 2)


# Sorting - Part 1 | Selection Sort, Bubble Sort, Insertion Sort | Strivers A2Z DSA Course

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_num = nums[i]
        index = i
        for j in range(i, n):
            if nums[j] < min_num:
                min_num = nums[j]
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    print(nums)


# Find Second Largest Element in Array | Remove duplicates from Sorted Array | Arrays Intro Video
def remove_duplicates(nums):
    i, j = 0, 1
    n = len(nums) - 1
    while j < n:
        while nums[i] == nums[j]:
            j += 1
        nums[i + 1] = nums[j]
        i += 1
    return i + 1


def rotate_array(nums, k):
    n = len(nums)
    temp = nums[:k]
    for i in range(k, n):
        nums[i - k] = nums[i]
    for i in range(n - k, n):
        nums[i] = temp[i - (n - k)]
    print(nums)
    


rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
