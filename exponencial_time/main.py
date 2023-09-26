import time


def exponential_example():
    pin = 541
    n = len(str(pin))
    start = time.time()

    for i in range(10 ** n):
        print(i)
        if i == pin:
            print(i)
            end = time.time()
            print(end - start)
            break


if __name__ == "__main__":
    exponential_example()
