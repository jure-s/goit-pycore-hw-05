def caching_fibonacci():

    cache = {}

    def fibonacci(n):

        if n <= 0:
            return 0
        elif n == 1:
            return 1

        if n in cache:
            print(f"{n} present in cache -> {cache[n]}")
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    fibonacci_fn = caching_fibonacci()

    while True:
        value = input("Type number or 'exit' to quit\n")

        if value == "exit":
            print("Exiting program...")
            break

        try:
            num = int(value)
            res = fibonacci_fn(num)
            print(f"Result: {res}")

        except ValueError:
            print("Wrong value! Please enter a valid integer.")
        except Exception as err:
            print(f"Something went wrong. Error: {err}")


if __name__ == "__main__":
    main()
