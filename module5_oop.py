
class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, count):
        for i in range(count):
            while True:
                try:
                    num = int(input(f"Enter number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Please enter a valid integer.")

    def find_number(self, target):
        try:
            index = self.numbers.index(target)
            return index + 1  # converting to 1-based index
        except ValueError:
            return -1

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
