def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()

