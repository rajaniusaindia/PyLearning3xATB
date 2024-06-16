# Task 2
# 2. Triangle Classifier
# 3. Fibanci series
    # fibanaci series
    # Program to display the Fibonacci sequence up to n
def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.
    Args:
        n (int): The number of terms to generate.
    Returns:
        list: A list containing the Fibonacci sequence up to the nth term.
    """
    # Initialize the Fibonacci sequence with the first two terms
    sequence = [0, 1]

    # Generate the remaining terms of the Fibonacci sequence
    n = int(input("Enter the value of n: "))
    print(n)
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
        print(sequence)



