import random  # For generating random inputs
import sys     # To access command-line arguments
import time    # To measure execution time

# Define different case types
CASES = ['Best', 'Worst', 'Average']

# Define input sizes to test
INPUT_SIZES = [1, 5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 120, 130, 140, 150, 160, 170]

SEED = 123  # Seed for reproducibility
ATTEMP_COUNT = 20  # Number of attempts for 'Average' case

def CmpeAlgorithm(arr):
    n = len(arr)
    res = 1
    for i in range(n):
        if arr[i] == 'c':
            for j in range(n, 0, -1):
                k = i + n
                for y in range(0, n, j):
                    k -= 1
                res += k
        elif arr[i] == 'm':
            z = 1
            while z < n:
                z *= 2
                res += z
        elif arr[i] == 'p':
            w = n
            res -= 1
            while w > 0:
                w //= 5
                res += 1
        elif arr[i] == 'e':
            for m in range(1, i + 1):
                p = m
                for l in range(m, n + 1):
                    for t in range(n, 0, -1):
                        p += t
                    res += p
    return res  # Return the result

def calcTime(arr):
    """
    Calculate execution time for each input array.
    """
    times = []
    for i in range(len(arr)):
        start = time.time()             # Start timer
        CmpeAlgorithm(arr[i])          # Run algorithm
        end = time.time()               # End timer
        elapsedTime = end - start       # Calculate elapsed time
        times.append(elapsedTime)       # Store the time
    return times  # Return all times

def printResult(size, case, times):
    """
    Print the average and individual execution times.
    """
    time_avg = sum(times) / len(times)  # Calculate average time
    print(f"Case: {case} Size: {size} Elapsed Time (s): {time_avg:.6f}")
    if case == 'Average':
        for i in range(len(times)):
            print(f"\tAttempt {i + 1} Elapsed Time (s): {times[i]:.6f}")
    print()  # Newline for readability

def generateRandomInput(n):
    """
    Generate a random input array of size n.
    """
    arr = []
    S = "cmmpeeee"  # Character distribution
    for _ in range(n):
        arr.append(S[random.randint(0, len(S) - 1)])
    return arr  # Return random array

def generateBestCase(n):
    """
    Generate the best-case input array.
    """
    arr = []
    arr.append('e')  # Start with 'e'
    for _ in range(n - 1):
        arr.append('p')  # Fill with 'p's
    return arr  # Return best-case array

def generateWorstCase(n):
    """
    Generate the worst-case input array.
    """
    arr = []
    arr.append('c')  # Start with 'c'
    for _ in range(n - 1):
        arr.append('e')  # Fill with 'e's
    return arr  # Return worst-case array

def main():
    """
    Main function to execute the program.
    """
    args = sys.argv[1:]  # Get command-line arguments

    # Set default values
    cases = CASES
    inputSizes = INPUT_SIZES
    seed = SEED
    attemptCount = ATTEMP_COUNT

    # Update defaults based on arguments
    if len(args) == 1:
        args[0] = args[0].lower().capitalize()
        if args[0] in CASES:
            cases = [args[0]]
        else:
            print("Invalid case type. Please enter one of the following: Best, Worst, Average")
            return
    if len(args) == 2:
        args[0] = args[0].lower().capitalize()
        try:
            inputSizes = [int(args[1])]
        except:
            print("Invalid input size. Please enter an integer value.")
            return
        if args[0] in CASES:
            cases = [args[0]]
        else:
            print("Invalid case type. Please enter one of the following: Best, Worst, Average")
            return
    if len(args) == 3:
        args[0] = args[0].lower().capitalize()
        try:
            inputSizes = [int(args[1])]
        except:
            print("Invalid input size. Please enter an integer value.")
            return
        try:
            attemptCount = int(args[2])
        except:
            print("Invalid attempt count. Please enter an integer value.")
            return
        if args[0] in CASES:
            cases = [args[0]]
        else:
            print("Invalid case type. Please enter one of the following: Best, Worst, Average")
            return
    if len(args) == 4:
        args[0] = args[0].lower().capitalize()
        try:
            inputSizes = [int(args[1])]
        except:
            print("Invalid input size. Please enter an integer value.")
            return
        try:
            attemptCount = int(args[2])
        except:
            print("Invalid attempt count. Please enter an integer value.")
            return
        try:
            seed = int(args[3])
        except:
            print("Invalid seed value. Please enter an integer value.")
            return
        if args[0] in CASES:
            cases = [args[0]]
        else:
            print("Invalid case type. Please enter one of the following: Best, Worst, Average")
            return
    if len(args) > 4:
        print("Invalid number of arguments. Please enter at most 4 arguments.")
        return

    random.seed(seed)  # Set the random seed

    # Iterate through each input size and case
    for size in inputSizes:
        for case in cases:
            if case == 'Best':
                arr = [generateBestCase(size)]  # Generate best case
            elif case == 'Worst':
                arr = [generateWorstCase(size)]  # Generate worst case
            elif case == 'Average':
                arr = []
                for _ in range(attemptCount):
                    arr.append(generateRandomInput(size))  # Generate average cases
            times = calcTime(arr)  # Calculate execution times
            printResult(size, case, times)  # Print the results

if __name__ == "__main__":
    main()  # Run the main function
