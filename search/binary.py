import time


def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1

    while last >= first:
        mid = (first + last)

        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


if __name__ == "__main__":
    a_list = [x*1 for x in range(1000000)]
    start = time.time()
    print(binary_search(a_list, 1))
    end = time.time()
    print(end - start)