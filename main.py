def is_even(num):
    return num % 2 == 0

nums = map(int, ["1", "2", "3", "4"])
even_nums = filter(is_even, nums)
print(list(even_nums))