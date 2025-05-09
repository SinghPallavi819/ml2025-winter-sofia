
from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    while True:
        try:
            n = int(input("Enter how many numbers you want to input: "))
            if n > 0:
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid positive integer.")

    processor.insert_numbers(n)

    while True:
        try:
            x = int(input("Enter a number to search for: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    result = processor.find_number(x)
    print(result)

if __name__ == "__main__":
    main()
