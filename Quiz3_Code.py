def multi(num1: int, num2: int) -> int:
    print(str(num1) + "*" + str(num2))
    return num1 * num2

def main():
    print("Starting Multiplication")
    print(multi(20, 11))
    print("Done")


if __name__ == "__main__":
    main()