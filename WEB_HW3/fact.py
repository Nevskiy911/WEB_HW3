
from collections import defaultdict

list_of_nums = []
divis = defaultdict(list)


def get_divisors(n):
    
    for div in range(1, n // 2 + 1):
        if n % div == 0:
            divis[n].append(div)
    divis[n].append(n)
    print(divis)
    return divis


def factorize():
    user_input = input("Get a num: ")
    us_in = user_input.split(", ")
    for el in us_in:
        list_of_nums.append(int(el))
        for el in list_of_nums:
            get_divisors(el)
    print(list_of_nums)


factorize()