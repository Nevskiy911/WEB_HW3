from time import time
from multiprocessing import Process


def factorize(*number):
    list_of_nums = []
    for n in number:
        temp_list = []
        for div in range(1, n + 1):
            if n % div == 0:
                temp_list.append(div)
        list_of_nums.append(temp_list)
    print(list_of_nums)
    return list_of_nums
# a, b, c, d = factorize(128, 255, 99999, 10651060)


def main():
    user_input = input("<<<Enter your numbers separated by commas and spaces (like: 111, 125)>>>: ")
    us_in = user_input.split(", ")
    for el in us_in:
        factorize(int(el))


if __name__ == "__main__":
    timer = time()
    main()
    process = []
    for i in range(4):
        pr = Process(target=factorize(), args=(f"Count process - {i}",))
        pr.start()
        process.append(pr)
    
    timer = time()
    [pr.join() for pr in process]
    print(f"Done for processes: {round(time() - timer, 4)}")
