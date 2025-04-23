def main():
    # user se num pochega aur usko int main convert krdega
    curr_value = int(input("Enter a number: "))

    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print the current value in the same line

if __name__ == '__main__':
    main()