# 3- Fibanaci series
# Program to display the Fibonacci sequence up to n
def fibonacci(n):
    sequence = [0, 1]

    # Generate the remaining terms of the Fibonacci sequence
    n = int(input("Enter the value of n: "))
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
        print(sequence)
