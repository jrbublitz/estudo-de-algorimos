import time


def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False


def create_list():
    print("Creating list ....")
    a_list = [x * 1 for x in range(1000000)]
    print("List ok ....")
    return a_list


if __name__ == "__main__":
    a_list = create_list()
    start = time.time()
    print(linear_search(a_list, 1))
    end = time.time()
    print(end - start)
