import random

N_NUMBERS: int = 10  # 10 numbers generate karne hain
MIN_VALUE: int = 1    # Minimum value 1
MAX_VALUE: int = 100  # Maximum value 100

def main():
    # generate 10 numbers and print on one line 
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  

if __name__ == '__main__':
    main()