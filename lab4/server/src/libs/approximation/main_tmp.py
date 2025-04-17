from libs.approximation.methods.linear import LinearMethod


def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    n = 5
    method = LinearMethod(x, y, n)
    result = method()

    print(result.parameters)


if __name__ == "__main__":
    main()
