import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":

    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    else:
        print("No command-line arguments detected.")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum : {result}")