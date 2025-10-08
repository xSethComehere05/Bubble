class BubbleSorter:
    def __init__(self, list):
        self.list = list

    def display(self):
        print(f"Current data: {self.list}")

    def sort(self):
        n = len(self.list)
        for i in range(0, n-1):
            for j in range(0, n - i - 1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
            print(f"After roubd {i+1}: {self.list}")

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 99]
    sorter = BubbleSorter(nums)

    print("Before Sorting:")
    sorter.display()

    sorter.sort()
    print("After sorting:")
    sorter.display()