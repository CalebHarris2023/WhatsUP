import random

def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

def sort_list(numbers):
    sorted_list = sorted(numbers)
    return sorted_list

if __name__ == "__main__":
    length = int(input("Enter the length of the random list: "))
    numbers = generate_random_list(length)
    print("Random list:", numbers)
    sorted_numbers = sort_list(numbers)
    print("Sorted list:", sorted_numbers)
