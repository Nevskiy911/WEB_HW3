list_of_nums = []
divis = []
user_input = input("Get a num: ")
us_in = user_input.split(",")
for el in us_in:
    list_of_nums.append(el)
print(list_of_nums)

def get_divisors():
    for i in list_of_nums:
        res = {1, i}
        for div in range(2, i // 2 + 1):
            if i % div == 0:
                res.add(div)
                divis.append(sorted(res))
    return divis

print(divis)
