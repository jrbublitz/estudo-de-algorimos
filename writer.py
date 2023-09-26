
if __name__ == "__main__":
    f = open("numbers.txt", "a")

    for i in range(1000000000):

        if i % 500000 == 0:
            print(f"Step -> {i}")

        f.write(f"{str(i)}\n")