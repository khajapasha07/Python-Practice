print("=== Prime Number Checker ===")

number = int(input("Enter a number: "))

if number > 1:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is not a Prime Number.")
else:
    print("Please enter a number greater than 1.")

print("\nProgram completed successfully!")
