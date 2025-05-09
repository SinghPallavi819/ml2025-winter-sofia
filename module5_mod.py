
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
            return index + 1  # 1-based index
        except ValueError:
            return -1
